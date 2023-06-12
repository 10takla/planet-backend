from .models import Transaction, Basket, Buying
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .serializers import BasketSerializer, BuyingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from planetService.serializers.serializers import PlotSerializer
from planetService.models import Plot
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from web3 import Web3
from rest_framework.status import HTTP_400_BAD_REQUEST

def check_transaction(transaction_hash):
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


    transaction = web3.eth.get_transaction_receipt(transaction_hash)

    if transaction is not None and transaction.blockNumber is not None:
        return True

    return False


class TransactionView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user

        amount = request.data.get('amount')
        transaction_hash = request.data.get('transactionHash')

        if transaction_hash and check_transaction(transaction_hash):
            payment = Transaction.objects.create(user=user, amount=amount, transaction_hash=transaction_hash)
            payment.save()

            user.wallet += amount
            user.save()

            return Response({'wallet': user.wallet})
        else:
            return Response({'message': 'Неверная транзакция'}, status=HTTP_400_BAD_REQUEST )



class BasketCreateView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Basket
    serializer_class = BasketSerializer

    def create(self, request, *args, **kwargs):
        plot_id = self.request.query_params.get('plot')
        user = self.request.user

        plot_query = Plot.objects.get(id=plot_id)
        buying = Basket.objects.create(user=user, plot=plot_query)
        sert = BasketSerializer(buying)
        return Response(sert.data, status=status.HTTP_201_CREATED)


class BasketDeleteView(DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Basket
    serializer_class = BasketSerializer
    lookup_url_kwarg = 'id_basket'

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BuyingCreateView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Buying
    serializer_class = BuyingSerializer

    def create(self, request, *args, **kwargs):
        plot_id = self.request.query_params.get('plot')
        user = self.request.user

        plot_query = Plot.objects.get(id=plot_id)
        plot_ser = PlotSerializer(plot_query, context={'fields': ['cost', 'owner', 'isSale']})
        plot = plot_ser.data
        cost = plot.get('cost')
        owner = plot.get('owner')
        isSale = plot.get('isSale')
        if owner and owner.get('id') == user.id:
            raise ValidationError("Вы не можете купить свой участок")
        if not isSale:
            raise ValidationError("Участок не продается")
        if user.wallet < cost:
            raise ValidationError("Недостаточно средств на балансе для покупки этого участка.")
        buying = Buying.objects.create(plot=plot_query, buyer=user, cost=cost, owner=owner.get('id') if owner else None)
        user.wallet -= cost
        user.save()
        sert = BuyingSerializer(buying, context={'request': self.request})
        return Response(sert.data, status=status.HTTP_201_CREATED)


class BuyingDeleteView(DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Buying
    serializer_class = BuyingSerializer
    lookup_url_kwarg = 'id_buying'

    def get_queryset(self):
        return Basket.objects.filter(buyer=self.request.user)
