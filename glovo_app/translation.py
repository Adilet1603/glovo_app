from .models import Product,Store,Category,Combo,Contact
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','description')

@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name','description','address')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Combo)
class ComboTranslationOptions(TranslationOptions):
    fields = ('combo_name','description')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)