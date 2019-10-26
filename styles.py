from openpyxl.styles import Border, Side, Alignment, Font

font = Font(name='Calibri',
            size=11,
            bold=True
            )
border_all = Border(left=Side(border_style='thin',
                              color='FF000000'),
                    right=Side(border_style='thin',
                               color='FF000000'),
                    top=Side(border_style='thin',
                             color='FF000000'),
                    bottom=Side(border_style='thin',
                                color='FF000000')
                    )

border_rls = Border(left=Side(border_style='thin',
                              color='FF000000'),
                    right=Side(border_style='thin',
                               color='FF000000')
                    )

border_top = Border(top=Side(border_style='thin',
                             color='FF000000'))

alignment = Alignment(horizontal='center',
                      vertical='center'
                      )
