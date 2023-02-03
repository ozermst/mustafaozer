from modeltranslation.translator import TranslationOptions, register, translator

from .models import FooterMenuBlock, FooterMenuItem


@register(FooterMenuBlock)
class FooterMenuBlockTranslationOptions(TranslationOptions):
    fields = ["heading"]


@register(FooterMenuItem)
class FooterMenuItemTranslationOptions(TranslationOptions):
    fields = ["link_title", "link_page"]


# translator.register(FooterMenuBlock1, FooterMenuBlock1TranslationOptions)
