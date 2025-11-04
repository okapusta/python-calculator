from marshmallow import Schema, ValidationError, fields, validate, validates_schema


class CalculationSchema(Schema):
    op = fields.Str(validate=validate.OneOf(["sum",  "subtract", "multiply", "divide"]), required=True)
    arg1 = fields.Integer(required=True)
    arg2 = fields.Integer(required=True)

    @validates_schema
    def validate_division_by_zero(self, data, **kwargs):
        if data.get('op') == 'divide' and data.get('arg2') == 0:
            raise ValidationError("cannot divide by zero", "arg2")
        pass
