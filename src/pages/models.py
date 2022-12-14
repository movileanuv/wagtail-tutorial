from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

from .blocks import PersonBlock


class HomePage(Page):
    subheading = RichTextField(blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('person', PersonBlock()),
        ('gallery', blocks.ListBlock(ImageChooserBlock(), template="blocks/gallery.html")),
        ('carousel', blocks.StreamBlock([
            ('image', ImageChooserBlock()),
            ('video', EmbedBlock()),
        ], template="blocks/carousel.html")),
    ], use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('body'),
    ]
