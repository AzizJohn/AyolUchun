from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(PostCategory, PostCategoryTranslationOptions)
