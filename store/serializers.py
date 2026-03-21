from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense, ExpenseEntry, Product, Category, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'category_id', 'image')


class ExpenseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseEntry
        fields = ('id', 'category', 'amount', 'expense')


class ExpenseSerializer(serializers.ModelSerializer):
    entries = ExpenseEntrySerializer(source='expense_entries', many=True, read_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'date', 'description', 'entries')


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = Order
        fields = ('id', 'product', 'product_id', 'quantity', 'order_date', 'ordered')
