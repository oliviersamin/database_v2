from django.core.management import BaseCommand
import os
import json
import datetime
from administrative.models import (
    InsuranceCompany,
    InsuranceContract,
    Document,
)
from finances.models import (
    BankCard,
    Bank,
    BankAccount
)
from real_estate.models import (
    Asset,
    CoproManagementContract,
    CoproManagementCompany,
    Mortgage,
    RentingManagementCompany,
    RentingManagementContract,
    Tenant
)

from tax.models import (
    Tax,
    TaxManagementCompany,
    TaxManagementContract
)
from transportation.models import (
    Asset
)
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    help = "Write in a txt file all the attributes for all models of all apps"
    MODELS = [
        InsuranceCompany,
        InsuranceContract,
        Document,
        BankCard,
        Bank,
        BankAccount,
        Asset,
        CoproManagementContract,
        CoproManagementCompany,
        Mortgage,
        RentingManagementCompany,
        RentingManagementContract,
        Tenant,
        Tax,
        TaxManagementCompany,
        TaxManagementContract,
    ]
    FILTERS = ['DoesNotExist', '__doc__', '__str__', '_meta', 'MultipleObjectsReturned', '__module__']
    FILE_PATH = os.environ.get('FILE_PATH_FOR_TELEGRAM')

    def get_details_for_one_model(self, model):
        module = model.__module__[:model.__module__.find('.')]
        index_start = model.__doc__.find("'") + 1
        index_stop = len(model.__doc__) - model.__doc__[::-1].find("'") - 1
        model_name = model.__doc__[index_start:index_stop]
        return "module: {}, model: {}, attributes: {}".\
            format(module, model_name, ';'.join([item for item in model.__dict__ if item not in self.FILTERS]))

    def get_all_models_details(self):
        result = ""
        print('|'.join([self.get_details_for_one_model(model) for model in self.MODELS]))
        return '|'.join([self.get_details_for_one_model(model) for model in self.MODELS])

    def handle(self, *args, **options):
        """
        "module: MODULE, model: MODEL, attributes: att1;att2;... | module: MODULE ..."
        """
        print('=' * 50 + ' GETTING ALL ATTRIBUTES ' + '=' * 50)
        results = self.get_all_models_details()
        with open(self.FILE_PATH, 'w') as file:
            file.write(results)
        print('=' * 50 + ' DONE ' + '=' * 50)
