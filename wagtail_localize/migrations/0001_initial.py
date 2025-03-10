# Generated by Django 3.0.6 on 2020-07-17 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0057_page_locale_fields_notnull"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="String",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_hash", models.UUIDField()),
                ("data", models.TextField()),
                (
                    "locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_strings",
                        to="wagtailcore.Locale",
                    ),
                ),
            ],
            options={
                "unique_together": {("locale", "data_hash")},
            },
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(unique=True)),
                ("template", models.TextField()),
                ("template_format", models.CharField(max_length=100)),
                ("string_count", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TranslatableObject",
            fields=[
                (
                    "translation_key",
                    models.UUIDField(primary_key=True, serialize=False),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
            options={
                "unique_together": {("content_type", "translation_key")},
            },
        ),
        migrations.CreateModel(
            name="TranslationSource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_repr", models.TextField(max_length=200)),
                ("content_json", models.TextField()),
                ("created_at", models.DateTimeField()),
                (
                    "locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Locale",
                    ),
                ),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sources",
                        to="wagtail_localize.TranslatableObject",
                    ),
                ),
                (
                    "specific_content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TranslationLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translation_logs",
                        to="wagtailcore.Locale",
                    ),
                ),
                (
                    "page_revision",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.PageRevision",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translation_logs",
                        to="wagtail_localize.TranslationSource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TranslationContext",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path_id", models.UUIDField()),
                ("path", models.TextField()),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtail_localize.TranslatableObject",
                    ),
                ),
            ],
            options={
                "unique_together": {("object", "path_id")},
            },
        ),
        migrations.CreateModel(
            name="TemplateSegment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="wagtail_localize.TranslationContext",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtail_localize.TranslationSource",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="segments",
                        to="wagtail_localize.Template",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StringSegment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                ("attrs", models.TextField(blank=True)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="wagtail_localize.TranslationContext",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtail_localize.TranslationSource",
                    ),
                ),
                (
                    "string",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="segments",
                        to="wagtail_localize.String",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RelatedObjectSegment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="wagtail_localize.TranslationContext",
                    ),
                ),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="references",
                        to="wagtail_localize.TranslatableObject",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtail_localize.TranslationSource",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StringTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "context",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="translations",
                        to="wagtail_localize.TranslationContext",
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="string_translations",
                        to="wagtailcore.Locale",
                    ),
                ),
                (
                    "translation_of",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="wagtail_localize.String",
                    ),
                ),
            ],
            options={
                "unique_together": {("locale", "translation_of", "context")},
            },
        ),
    ]
