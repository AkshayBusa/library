from __future__ import unicode_literals

from django.db import models


class Authors(models.Model):
    author = models.ForeignKey('BookAuthors', models.DO_NOTHING, db_column='Author_id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    class Meta:
        managed = False
        db_table = 'authors'


class Book(models.Model):
    isbn = models.CharField(db_column='Isbn', primary_key=True, max_length=10)
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)
    availability = models.IntegerField(db_column='Availability')

    class Meta:
        managed = False
        db_table = 'book'


class BookAuthors(models.Model):
    author_id = models.AutoField(db_column='Author_id', primary_key=True)
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='Isbn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_authors'


class BookLoans(models.Model):
    loan_id = models.AutoField(db_column='Loan_id', primary_key=True)
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='Isbn', blank=True, null=True)
    card = models.ForeignKey('Borrower', models.DO_NOTHING, db_column='Card_id', blank=True, null=True)
    date_out = models.DateField(db_column='Date_out', blank=True, null=True)
    due_date = models.DateField(db_column='Due_date', blank=True, null=True)
    date_in = models.DateField(db_column='Date_in', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_loans'


class Borrower(models.Model):
    card_id = models.AutoField(db_column='Card_id', primary_key=True)
    ssn = models.CharField(db_column='Ssn', unique=True, max_length=9)
    bname = models.CharField(db_column='Bname', max_length=255, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrower'