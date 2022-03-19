from django.contrib import admin

from .models import Flat, Claim
# from .models import Flat


# @admin.register(Flat)
# class FlatAdmin(admin.ModelAdmin):
#     search_fields = ('town', 'address', 'owner')
#     readonly_fields = ['created_at']
#     list_display = ['address', 'price', 'construction_year', 'new_building', 'town']
#     list_editable = ['new_building']
#     list_filter = ['new_building', 'rooms_number', 'has_balcony']
#     # raw_id_fields = ('author_like',)


# @admin.register(Claim)
# class ClaimAdmin(admin.ModelAdmin):
#     raw_id_fields = ('flat', 'author')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'construction_year', 'new_building', 'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('author_like',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'author')









