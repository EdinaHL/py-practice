from decimal import Decimal


class Area:

    area_units_list = ["sq cm (square centimeters)", "sq m (square meters)", "sq ft (square foot)"
        , "ac (acres)", "ha (hectares)"]

    # Base of conversion: sq cm

    def __init__(self):
        self.source_exchanged_to_sqcm = Decimal()
        self.to_unit = ""
        self.from_unit = ""
        self.user_input = Decimal()
        self.sqcm_exchanged_to_target = Decimal()

    def from_this_unit(self, unit):
        self.from_unit = unit

    def to_this_unit(self, unit):
        self.to_unit = unit

    def user_input_value(self, value):
        try:
            self.user_input = Decimal(value)
        except:
            return "Invalid Number"

    def return_result(self):
        return round(self.sqcm_exchanged_to_target, 4)

    def from_source_to_sqcm(self):
        match self.from_unit:
            case "sq cm (square centimeters)": self.source_exchanged_to_sqcm = self.user_input
            case "sq m (square meters)": self.source_exchanged_to_sqcm = self.user_input * Decimal("10000")
            case "sq ft (square foot)": self.source_exchanged_to_sqcm = self.user_input * Decimal("929")
            case "ac (acres)": self.source_exchanged_to_sqcm = self.user_input * Decimal("40468564")
            case "ha (hectares)": self.source_exchanged_to_sqcm = self.user_input * Decimal("100000000")

    def from_sqcm_to_target_unit(self):
        match self.to_unit:
            case "mg (milligrams)" : self.sqcm_exchanged_to_target = self.source_exchanged_to_sqcm
            case "sq m (square meters)": self.sqcm_exchanged_to_target = self.source_exchanged_to_sqcm / Decimal("10000")
            case "sq ft (square foot)": self.sqcm_exchanged_to_target = self.source_exchanged_to_sqcm / Decimal("929")
            case "ac (acres)": self.sqcm_exchanged_to_target = self.source_exchanged_to_sqcm / Decimal("40468564")
            case "ha (hectares)": self.sqcm_exchanged_to_target = self.source_exchanged_to_sqcm / Decimal("100000000")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_sqcm()
        self.from_sqcm_to_target_unit()
        self.return_result()