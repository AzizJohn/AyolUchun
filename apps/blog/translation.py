from modeltranslation.translator import translator, TranslationOptions
from .models import *



class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'profession')


translator.register(PostCategory, PostCategoryTranslationOptions)
