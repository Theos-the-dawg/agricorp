from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.dateparse import parse_date
from .models import Expense, ExpenseEntry, Product, Category, Order
from .serializers import (
    UserSerializer, UserRegistrationSerializer, ProductSerializer,
    CategorySerializer, ExpenseSerializer, ExpenseEntrySerializer,
    OrderSerializer
)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """User registration endpoint"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"detail": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    """Dashboard data endpoint"""
    user = request.user
    expenses = ExpenseEntry.objects.filter(reporter=user)
    products = Product.objects.all()
    orders = Order.objects.filter(product__in=products)

    total_expenses = sum(e.amount for e in expenses)
    recent_expenses = ExpenseEntry.objects.filter(reporter=user).values(
        'id', 'category', 'amount', 'expense__date'
    ).order_by('-expense__date')[:5]

    data = {
        'totalExpenses': float(total_expenses),
        'totalProducts': products.count(),
        'totalOrders': orders.count(),
        'recentExpenses': list(recent_expenses)
    }
    return Response(data)


class ProductViewSet(viewsets.ModelViewSet):
    """Product ViewSet"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """Category ViewSet"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ExpenseEntryViewSet(viewsets.ModelViewSet):
    """Expense Entry ViewSet"""
    serializer_class = ExpenseEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseEntry.objects.filter(reporter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    """Order ViewSet"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_expenses(request):
    """Get all expenses for the current user"""
    expenses = ExpenseEntry.objects.filter(reporter=request.user).values(
        'id', 'category', 'amount', 'expense__date'
    ).order_by('-expense__date')
    
    return Response(list(expenses))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_expense(request):
    """Create a new expense entry"""
    expense_date = request.data.get('date')
    if expense_date:
        parsed_date = parse_date(expense_date)
        if parsed_date is None:
            return Response({'date': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        parsed_date = timezone.now().date()

    expense, _ = Expense.objects.get_or_create(date=parsed_date)

    entry_data = {
        'category': request.data.get('category'),
        'amount': request.data.get('amount')
    }

    serializer = ExpenseEntrySerializer(data=entry_data)
    if serializer.is_valid():
        serializer.save(reporter=request.user, expense=expense)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    """Get all products"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

