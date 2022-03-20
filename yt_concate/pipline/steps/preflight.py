from .step import Step


class PreFlight(Step):
    def process(self, data, inputs, utils):
        utils.create_dirs()
