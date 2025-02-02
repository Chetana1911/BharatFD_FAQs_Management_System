from django.db import models
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator
from django.core.exceptions import ValidationError

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
   

    def get_translated_question(self, lang):
        """Dynamically retrieve translated question."""
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang, self.question)  # Fallback to English

    def clean(self):
        """Validate model data."""
        if not self.question:
            raise ValidationError("Question cannot be empty.")
        if len(self.question) > 5000:
            raise ValidationError("Question must be a maximum of 5000 characters.")

    def save(self, *args, **kwargs):
        """Automate translations during object creation."""
        self.clean()  # Run validation before saving
        
        try:
            # Translate to Hindi
            if not self.question_hi:
                translated_hi = GoogleTranslator(source='auto', target='hi').translate(self.question)
                if translated_hi:  # Ensure translation is not empty
                    self.question_hi = translated_hi
                else:
                    raise Exception("Hindi translation failed or returned empty.")

            # Translate to Bengali
            if not self.question_bn:
                translated_bn = GoogleTranslator(source='auto', target='bn').translate(self.question)
                if translated_bn:  # Ensure translation is not empty
                    self.question_bn = translated_bn
                else:
                    raise Exception("Bengali translation failed or returned empty.")

        except Exception as e:
            print(f"Translation failed: {e}")  # Log the error
            # Fallback to English if translation fails
            self.question_hi = self.question_hi or self.question
            self.question_bn = self.question_bn or self.question
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question










