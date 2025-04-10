from datetime import date
import json
from dataclasses import dataclass, field, asdict
from functools import lru_cache

@dataclass
class Customer:
    name: str
    contact_information: str
    company: str
    
    @lru_cache(maxsize=None)
    def serialize(self):
        return json.dumps(asdict(self))

@dataclass
class Deal:
    customer: Customer
    amount: float
    status: str
    description: str
    
    @lru_cache(maxsize=None)
    def serialize(self):
        deal_dict = asdict(self)
        deal_dict['customer'] = json.loads(deal_dict['customer'].serialize())
        return json.dumps(deal_dict)

@dataclass
class Interaction:
    customer: Customer
    interaction_date: date
    notes: str
    
    @lru_cache(maxsize=None)
    def serialize(self):
        interaction_dict = asdict(self)
        interaction_dict['interaction_date'] = interaction_dict['interaction_date'].isoformat()
        interaction_dict['customer'] = json.loads(interaction_dict['customer'].serialize())
        return json.dumps(interaction_dict)