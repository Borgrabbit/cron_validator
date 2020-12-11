import re


class FormatException(Exception):
    pass


class CronValidator(object):
    _expression = ''

    _cron_days = {
        0: 'SUN',
        1: 'MON',
        2: 'TUE',
        3: 'WED',
        4: 'THU',
        5: 'FRI',
        6: 'SAT'
    }

    _cron_months = {
        1: 'JAN',
        2: 'FEB',
        3: 'MAR',
        4: 'APR',
        5: 'MAY',
        6: 'JUN',
        7: 'JUL',
        8: 'AUG',
        9: 'SEP',
        10: 'OCT',
        11: 'NOV',
        12: 'DEC'
    }

    def validate_expression(self, expression_parts):
        print('validate expr ', expression_parts)
        # print('validate expr ', expression_parts[0])
        # print('validate expr ', expression_parts[1])
        # print('validate expr ', expression_parts[2])
        # print('validate expr ', expression_parts[3])
        # print('validate expr ', expression_parts[4])
        # print('validate expr ', expression_parts[5])
        # print('validate expr ', expression_parts[6])
        """ SEC and MIN """
        # test_expr = "*/69"
        # if re.fullmatch("\d{1,2}$", test_expr):
        #     self.check_value_limit(expr=test_expr, mi=0, mx=59, prefix='Second and Minute')
        #     print(f'rx {test_expr}')
        # elif re.search(r"[-*,/]", test_expr):
        #     print(f'sec/min special character ')
        #     if re.fullmatch(r"\d{1,2}-\d{1,2}$", test_expr):
        #         print(f'n-n {test_expr}')
        #         temp = test_expr.split("-")
        #         self.check_value_limit(expr=temp[0], mi=0, mx=59, prefix='Second and Minute')
        #         self.check_value_limit(expr=temp[1], mi=0, mx=59, prefix='Second and Minute')
        #         self.compare_range(st=temp[0], ed=temp[1], mi=0, mx=59, prefix='Second and Minute')
        #     elif re.fullmatch(r"\d{1,2}/\d{1,2}$", test_expr):
        #         print(f'n/n {test_expr}')
        #         temp = test_expr.split("/")
        #         self.check_value_limit(expr=temp[0], mi=0, mx=59, prefix='Second and Minute')
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=59, prefix='Second and Minute')
        #     elif re.fullmatch(r"\*/\d{1,2}$", test_expr):
        #         print("*/n ", test_expr)
        #         temp = test_expr.split("/")
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=59, prefix='Second and Minute')
        #     elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", test_expr):
        #         print(f'n,n {test_expr}')
        #         expr_list = test_expr.split(",")
        #         if len(expr_list) > 60:
        #             exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(60, len(expr_list))
        #             raise FormatException(exception_msg)
        #         else:
        #             for n in test_expr.split(","):
        #                 self.check_value_limit(expr=n, mi=0, mx=59, prefix='Second and Minute')
        #     elif '*' == test_expr:
        #         print(f'* {test_expr}')
        #         pass
        #     else:
        #         exception_msg = "Illegal Expression Format {}".format(test_expr)
        #         raise FormatException(exception_msg)
        # else:
        #     print(f'Unknown match {test_expr}')
        #     exception_msg = "Illegal Expression Format {}".format(test_expr)
        #     raise FormatException(exception_msg)
        #
        # print("sec,min RX:: ", test_expr)

        """ HRS """
        # test_expr_hr = '0'
        # if re.fullmatch("\d{1,2}$", test_expr_hr):
        #     print("hrs 1")
        #     self.check_value_limit(expr=test_expr_hr, mi=0, mx=23, prefix='Hour')
        # elif re.search(r"[-*,/]", test_expr_hr):
        #     print(f'hrs special character ')
        #     if re.fullmatch(r"\d{1,2}-\d{1,2}$", test_expr_hr):
        #         print(f'n-n {test_expr_hr}')
        #         temp = test_expr_hr.split("-")
        #         self.check_value_limit(expr=temp[0], mi=0, mx=23, prefix='Hour')
        #         self.check_value_limit(expr=temp[1], mi=0, mx=23, prefix='Hour')
        #         self.compare_range(st=temp[0], ed=temp[1], mi=0, mx=23, prefix='Hour')
        #     elif re.fullmatch(r"\d{1,2}/\d{1,2}$", test_expr_hr):
        #         print(f'n/n {test_expr_hr}')
        #         temp = test_expr_hr.split("/")
        #         self.check_value_limit(expr=temp[0], mi=0, mx=23, prefix='Hour')
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=23, prefix='Hour')
        #     elif re.fullmatch(r"\*/\d{1,2}$", test_expr_hr):
        #         print("*/n ", test_expr_hr)
        #         temp = test_expr_hr.split("/")
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=23, prefix='Hour')
        #     elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", test_expr_hr):
        #         print(f'n,n {test_expr_hr}')
        #         test_expr_hr_list = test_expr_hr.split(",")
        #         if len(test_expr_hr_list) > 24:
        #             exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(24, len(test_expr_hr_list))
        #             raise FormatException(exception_msg)
        #         else:
        #             for n in test_expr_hr.split(","):
        #                 self.check_value_limit(expr=n, mi=0, mx=23, prefix='Hour')
        #     else:
        #         exception_msg = "Illegal Expression Format {}".format(test_expr_hr)
        #         raise FormatException(exception_msg)
        # else:
        #     print(f'Unknown match {test_expr_hr}')
        #     exception_msg = "Illegal Expression Format {}".format(test_expr_hr)
        #     raise FormatException(exception_msg)

        """ MON """
        # expr_month = '33,2,3,4,5,MAR,7,8,9,10,11,1'
        # if re.fullmatch("\d{1,2}$", expr_month):
        #     self.check_value_limit(expr=expr_month, mi=1, mx=12, prefix='Month')
        # elif re.fullmatch(r"\D{3}", expr_month):
        #     matched_month = [m for m in self._cron_months.values() if expr_month == m]
        #     if len(matched_month) == 0:
        #         exception_msg = "Invalid Month value '{}'".format(expr_month)
        #         raise FormatException(exception_msg)
        #
        # elif re.search(r"[-*,/]", expr_month):
        #     print(f'month special character ')
        #     if re.fullmatch(r"\d{1,2}-\d{1,2}$", expr_month):
        #         print(f'n-n {expr_month}')
        #         temp = expr_month.split("-")
        #         self.check_value_limit(expr=temp[0], mi=1, mx=12, prefix='Month')
        #         self.check_value_limit(expr=temp[1], mi=1, mx=12, prefix='Month')
        #         self.compare_range(st=temp[0], ed=temp[1], mi=1, mx=12, prefix='Month')
        #     elif re.fullmatch(r"\D{3}-\D{3}$", expr_month):
        #         print(f'str-str {expr_month}')
        #         temp = expr_month.split("-")
        #         cron_months = {v: k for (k, v) in self._cron_months.items()}
        #         st_not_exist = temp[0] not in cron_months
        #         ed_not_exist = temp[1] not in cron_months
        #         if st_not_exist or ed_not_exist:
        #             exception_msg = "Invalid Month value '{}'".format(expr_month)
        #             raise FormatException(exception_msg)
        #         self.compare_range(st=cron_months[temp[0]], ed=cron_months[temp[1]], mi=1, mx=12, prefix='Month')
        #     elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr_month):
        #         print(f'n/n {expr_month}')
        #         temp = expr_month.split("/")
        #         self.check_value_limit(expr=temp[0], mi=1, mx=12, prefix='Month')
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=12, prefix='Month')
        #     elif re.fullmatch(r"\*/\d{1,2}$", expr_month):
        #         print("*/n ", expr_month)
        #         temp = expr_month.split("/")
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=12, prefix='Month')
        #     elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr_month):
        #         print(f'n,n: {expr_month}')
        #         expr_month_list = expr_month.split(",")
        #         if len(expr_month_list) > 12:
        #             exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(12, len(expr_month_list))
        #             raise FormatException(exception_msg)
        #         else:
        #             for month in expr_month.split(","):
        #                 self.check_value_limit(expr=month, mi=1, mx=12, prefix='Month')
        #     elif re.fullmatch(r"^(\d{1,2}|\D{3})((,\d{1,2})+|(,\D{3})*)*", expr_month):
        #         print(f'n|str,n|str: {expr_month}')
        #         expr_month_list = expr_month.split(",")
        #         if len(expr_month_list) > 12:
        #             exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(12, len(expr_month_list))
        #             raise FormatException(exception_msg)
        #         else:
        #             cron_months = {v: k for (k, v) in self._cron_months.items()}
        #             for month in expr_month.split(","):
        #                 print(f'month n|str {month} { isinstance(month, str) }')
        #                 month = cron_months[month] if len(month) == 3 else month
        #                 self.check_value_limit(expr=month, mi=1, mx=12, prefix='Month')
        #     else:
        #         exception_msg = "Illegal Expression Format {}".format(expr_month)
        #         raise FormatException(exception_msg)
        # else:
        #     print(f'Unknown match {expr_month}')
        #     exception_msg = "Illegal Expression Format {}".format(expr_month)
        #     raise FormatException(exception_msg)

        """ YEAR """
        expr_year = '2000,2001,1970'
        if re.fullmatch("\d{4}$", expr_year):
            print("year 1")
            self.check_value_limit(expr=expr_year, mi=1970, mx=2099, prefix='Year')
        elif re.search(r"[-*,/]", expr_year):
            print(f'year special character ')
            if re.fullmatch(r"\d{4}-\d{4}$", expr_year):
                print(f'n-n {expr_year}')
                temp = expr_year.split("-")
                self.check_value_limit(expr=temp[0], mi=1970, mx=2099, prefix='Year')
                self.check_value_limit(expr=temp[1], mi=1970, mx=2099, prefix='Year')
                self.compare_range(st=temp[0], ed=temp[1], mi=1970, mx=2099, prefix='Year')
            elif re.fullmatch(r"\d{4}/\d{1,3}$", expr_year):
                print(f'n/n {expr_year}')
                temp = expr_year.split("/")
                self.check_value_limit(expr=temp[0], mi=1970, mx=2099, prefix='Year')
                self.check_value_limit('interval', expr=temp[1], mi=0, mx=129, prefix='Year')
            elif re.fullmatch(r"\*/\d{1,3}$", expr_year):
                print("*/n ", expr_year)
                temp = expr_year.split("/")
                self.check_value_limit('interval', expr=temp[1], mi=0, mx=129, prefix='Year')
            elif re.fullmatch(r"^\d{4}(,\d{4})+", expr_year):
                print(f'n,n {expr_year}')
                expr_year_list = expr_year.split(",")
                if len(expr_year_list) > 84:
                    exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(84, len(
                        expr_year_list))
                    raise FormatException(exception_msg)
                else:
                    for year in expr_year.split(","):
                        self.check_value_limit(expr=year, mi=1970, mx=2099, prefix='Year')
            else:
                exception_msg = "Illegal Expression Format {}".format(expr_year)
                raise FormatException(exception_msg)
        else:
            print(f'Unknown match {expr_year}')
            exception_msg = "Illegal Expression Format {}".format(expr_year)
            raise FormatException(exception_msg)

        """ DAY of Month 
        # n  - ?
        # n-n - ?
        # n/n - ? -> */n
        # n,n,n - ?
        # L - ?
        # LW - ?
        # L-n{1,2} - ?
        # n{1,2}W - ?
        """
        # expr_day = 'LW'
        # if re.fullmatch("\d{1,2}$", expr_day):
        #     print("expr_day 1")
        #     self.check_value_limit(expr=expr_day, mi=1, mx=31, prefix='Day')
        # elif re.search(r"[-*,/]", expr_day):
        #     print(f'expr_day special character ')
        #     if re.fullmatch(r"\d{1,2}-\d{1,2}$", expr_day):
        #         print(f'n-n {expr_day}')
        #         temp = expr_day.split("-")
        #         self.check_value_limit(expr=temp[0], mi=1, mx=31, prefix='Day')
        #         self.check_value_limit(expr=temp[1], mi=1, mx=31, prefix='Day')
        #         self.compare_range(st=temp[0], ed=temp[1], mi=1, mx=31, prefix='Day')
        #     elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr_day):
        #         print(f'n/n {expr_day}')
        #         temp = expr_day.split("/")
        #         self.check_value_limit(expr=temp[0], mi=1, mx=31, prefix='Day')
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=31, prefix='Day')
        #     elif re.fullmatch(r"\*/\d{1,2}$", expr_day):
        #         print("*/n ", expr_day)
        #         temp = expr_day.split("/")
        #         self.check_value_limit('interval', expr=temp[1], mi=0, mx=31, prefix='Day')
        #     elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr_day):
        #         print(f'n,n {expr_day}')
        #         expr_day_list = expr_day.split(",")
        #         if len(expr_day_list) > 31:
        #             exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(31, len(expr_day_list))
        #             raise FormatException(exception_msg)
        #         else:
        #             for dayofmonth in expr_day.split(","):
        #                 self.check_value_limit(expr=dayofmonth, mi=1, mx=31, prefix='Day')
        #     else:
        #         exception_msg = "Illegal Expression Format {}".format(expr_day)
        #         raise FormatException(exception_msg)
        # elif re.fullmatch(r"^(L|l)(W|w)?$", expr_day):
        #     print(f'L or LW  == {expr_day}')
        # elif re.fullmatch(r"^(\d{1,2})(w{1}|W{1})$", expr_day):
        #     print(f'nW == {expr_day}')
        #     self.check_value_limit(expr=expr_day[:-1], mi=1, mx=31, prefix='Day')
        # else:
        #     print(f'Unknown match {expr_day}')
        #     exception_msg = "Illegal Expression Format {}".format(expr_day)
        #     raise FormatException(exception_msg)

        """ DAY of Week field
        # ? - * n sss
        # ? - n-n, sss-sss
        # ? - n/n -> */n
        # ? - /D{1,3},/D{1,3}
        # ? - nL
        # ? - n#n
        """
        expr_dow = '7#6'
        if re.fullmatch("\d{1}$", expr_dow):
            print("expr_dow 1")
            self.check_value_limit(expr=expr_dow, mi=1, mx=7, prefix='DayOfWeek')
        elif re.fullmatch("\D{3}", expr_dow):
            print(f'expr_day special character ')
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            print(f'crondays {expr_dow.upper() in cron_days}')
            if expr_dow.upper() in cron_days:
                pass
            else:
                msg = "Invalid DayOfWeek value '{}'".format(expr_dow)
                raise FormatException(msg)
        elif re.fullmatch(r"\d{1}/\d{1}$", expr_dow):
            print(f'n/n {expr_dow}')
            temp = expr_dow.split("/")
            self.check_value_limit(expr=temp[0], mi=1, mx=7, prefix='DayOfWeek')
            self.check_value_limit(expr=temp[1], mi=1, mx=7, prefix='DayOfWeek')
        elif re.fullmatch(r"[*]/\d{1}$", expr_dow):
            print(f'*/n {expr_dow}')
            temp = expr_dow.split("/")
            self.check_value_limit(expr=temp[1], mi=1, mx=7, prefix='DayOfWeek')
        elif re.fullmatch(r"\d{1}-\d{1}$", expr_dow):
            print(f'n-n {expr_dow}')
            temp = expr_dow.split("-")
            self.check_value_limit(expr=temp[0], mi=1, mx=7, prefix='DayOfWeek')
            self.check_value_limit(expr=temp[1], mi=1, mx=7, prefix='DayOfWeek')
            self.compare_range(st=temp[0], ed=temp[1], mi=1, mx=7, prefix='DayOfWeek')
        elif re.fullmatch(r"\D{3}-\D{3}$", expr_dow):
            print(f'sss-sss {expr_dow}')
            temp = expr_dow.split("-")
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            try:
                st_day = cron_days[temp[0].upper()]
                ed_day = cron_days[temp[1].upper()]
            except KeyError:
                msg = "Invalid DayOfWeek value '{}'".format(expr_dow)
                raise FormatException(msg)
            self.compare_range(st=st_day, ed=ed_day, mi=1, mx=7, prefix='DayOfWeek', exception_type='dow')
        elif re.fullmatch(r"^(\d{1}|\D{3})((,\d{1})+|(,\D{3})*)*", expr_dow):
            print(f'n,n {expr_dow}')
            expr_dow_list = expr_dow.split(",")
            if len(expr_dow_list) > 7:
                exception_msg = "Exceeded maximum number({0}) of specified value. '{1}' is provided".format(7, len(expr_dow_list))
                raise FormatException(exception_msg)
            else:
                cron_days = {v: k for (k, v) in self._cron_days.items()}
                for day in expr_dow.split(","):
                    print(f'month n|str {day} { isinstance(day, str) }')
                    day = cron_days[day.upper()] + 1 if len(day) == 3 else day # syncronize by add 1 to cron_days index
                    self.check_value_limit(expr=day, mi=1, mx=7, prefix='DayOfWeek')
        elif re.fullmatch(r"\d{1}(l|L)", expr_dow):
            print(f'nL {expr_dow}')
            self.check_value_limit(expr=expr_dow[0], mi=1, mx=7, prefix='DayOfWeek')
            expr_dow[0]
        elif re.fullmatch(r"\d{1}#\d{1}", expr_dow):
            print(f'n#n {expr_dow}')
            temp = expr_dow.split('#')
            self.check_value_limit(expr=temp[0], mi=1, mx=7, prefix='DayOfWeek')
            self.check_value_limit(expr=temp[1], mi=1, mx=5, prefix='DayOfWeek', exception_type='dow')
        # elif check * / - , L #

    def check_value_limit(self, exception_type=None, **kwargs):
        print('KWARGS :: ', kwargs)
        prefix = kwargs["prefix"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        expr = kwargs["expr"]
        if int(expr) < mi or mx < int(expr):
            if exception_type is None:
                exception_msg = "{0} values must be between {1} and {2} but '{3}' is provided".format(prefix, mi, mx,
                                                                                                      expr)
            elif exception_type == "interval":
                exception_msg = "({0}) Accepted increment value range is {1}~{2} but '{3}' is provided".format(prefix,
                                                                                                               mi, mx,
                                                                                                               expr)
            raise FormatException(exception_msg)
        else:
            pass

    def compare_range(self, exception_type=None, **kwargs):
        prefix = kwargs["prefix"]
        st = kwargs["st"]
        ed = kwargs["ed"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        print(f'st {st}, ed {ed} {int(st) < int(ed)}')
        if int(st) > int(ed):
            if exception_type is None:
                exception_msg = "({0}) Invalid range '{1}-{2}'. Accepted range is {3}-{4}".format(prefix, st, ed, mi,
                                                                                                  mx)
            raise FormatException(exception_msg)

