
class MyAutoTemplateDescriptionHandler:
    def __init__(self, lot_number):
        self.lot_number = lot_number

    def get_description(self):
        with open('description_templates/header.txt', "r", encoding="utf-8") as header_file:
            header_text = header_file.read()

        with open('description_templates/footer.txt', "r", encoding="utf-8") as footer_file:
            footer_text = footer_file.read()

        return header_text + '\n' +self.lot_number + '\n' + footer_text

