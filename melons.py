"""This file should have our order classes in it."""
import random

class AbstractMelonOrder(object):
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()

        if self.species == "Christmas Melon":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price
        return total


    def get_base_price(self):
        """Calculates price during splurge pricing"""
        base_price = random.randrange(5, 10)
        return base_price
        
      
    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', .08)
        
        
        
        



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(speciorder = 
        self.country_code = country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return total + 3

    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code



class GovernmentMelonOrder(AbstractMelonOrder):
    """Government orders have 0 tax"""
    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, 'government', 0 )
        self.passed_inspection = False

    def mark_inspection(self):
        """Set shipped to true."""

        self.passed_inspection = True