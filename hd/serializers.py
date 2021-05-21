from rest_framework import serializers
from .models import HdPlusSubscription,HdRegistration



class Hd_Plus_Authentication_serializer(serializers.Serializer):
	hd_plus_number		=		serializers.CharField(max_length=120)
	ott_password 		=		serializers.CharField(max_length=120)



class HdPlusSubscriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	HdPlusSubscription
		fields 	=	"__all__"