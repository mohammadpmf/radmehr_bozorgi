from enum import Enum

class DiscountTypeEnum(Enum):
    PERCENTAGE = 'درصدی'
    FIXED_AMOUNT = 'مبلغی'

# دسترسی به یکی از اعضای Enum
t = DiscountTypeEnum.PERCENTAGE
print(type(t.name), t.name)
print(type(t.value), t.value)