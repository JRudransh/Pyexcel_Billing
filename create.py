from openpyxl import Workbook
import os
from values import sheet_start_from
pos1 = sheet_start_from
pos2 = pos1 + 3
pos3 = pos2 + 1


class CreateNewExcelFile:
    def __init__(self, pos4=pos3 + 10, name="prj_main"):
        # Create new workbook
        self.wb = Workbook()
        self.sheet = "Billing"
        ws = self.wb.create_sheet(self.sheet, 0)

        # For Name Phone NO & Address
        [ws.merge_cells(f"A{i}:D{i}") for i in range(pos1, pos2)]

        # For Product List with Heading
        [ws.merge_cells(f"B{i}:D{i}") for i in range(pos3, pos4)]

        # For Date Row
        ws.merge_cells("F3:G3")

        # For Serial No Row
        ws.merge_cells("F5:G5")

        # For Something
        ws.merge_cells("B21:G21")

        # To Save
        self.wb.save(f"{name}.xlsx")

        # For Basic Security
        os.rename(f"{name}.xlsx", f"{name}.bak")



