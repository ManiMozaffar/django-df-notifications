from df_notifications.models import PushAction
from df_notifications.models import PushActionCategory
from df_notifications.models import UserDevice
from fcm_django.api.rest_framework import FCMDeviceSerializer
from rest_framework import serializers


class UserDeviceSerializer(FCMDeviceSerializer):
    class Meta(FCMDeviceSerializer.Meta):
        model = UserDevice
        fields = FCMDeviceSerializer.Meta.fields


class PushActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushAction
        fields = (
            "name",
            "button_text",
            "authentication_required",
            "destructive",
            "foreground",
        )


class PushActionCategorySerializer(serializers.ModelSerializer):
    actions = PushActionSerializer(many=True)

    class Meta:
        model = PushActionCategory
        fields = (
            "name",
            "actions",
        )
