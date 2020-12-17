import re

expr_ls = [
    # '* * * 8 *'
    '* * * 1 * 1',
    '* * * ? * * *',
    '0 * * ? * *',
    '0 */2 * ? * *',
    '0 1/2 * ? * *',
    '0 */2 * ? * *',
    '0 */3 * ? * *',
    '0 */4 * ? * *',
    '0 */5 * ? * *',
    '0 */10 * ? * *',
    '0 */15 * ? * *',
    '0 */30 * ? * *',
    '0 15,30,45 * ? * *',
    '0 0 * ? * *',
    '0 0 */2 ? * *',
    '0 0 1/2 ? * *',
    '0 0 1/2 ? * *',
    '0 0 */3 ? * *',
    '0 0 */4 ? * *',
    '0 0 */6 ? * *',
    '0 0 */8 ? * *',
    '0 0 */12 ? * *',
    '0 0 0 * * ?',
    '0 0 1 * * ?',
    '0 0 6 * * ?',
    '0 0 12 * * ?',
    '0 0 12 * * ?',
    '0 0 12 ? * SUN',
    '0 0 12 ? * MON',
    '0 0 12 ? * TUE',
    '0 0 12 ? * WED',
    '0 0 12 ? * THU',
    '0 0 12 ? * FRI',
    '0 0 12 ? * SAT',
    '0 0 12 ? * MON-FRI',
    '0 0 12 ? * SUN,SAT',
    '0 0 12 */7 * ?',
    '0 0 12 1 * ?',
    '0 0 12 2 * ?',
    '0 0 12 15 * ?',
    '0 0 12 1/2 * ?',
    '0 0 12 1/4 * ?',
    '0 0 12 L * ?',
    '0 0 12 L-2 * ?',
    '0 0 12 LW * ?',
    '0 0 12 1L * ?',
    '0 0 12 2L * ?',
    '0 0 12 6L * ?',
    '0 0 12 1W * ?',
    '0 0 12 15W * ?',
    '0 0 12 ? * 2#1',
    '0 0 12 ? * 6#1',
    '0 0 12 ? * 2#2',
    '0 0 12 ? * 5#3',
    '0 0 12 ? JAN *',
    '0 0 12 ? JUN *',
    '0 0 12 ? JAN,JUN *',
    '0 0 12 ? DEC *',
    '0 0 12 ? JAN,FEB,MAR,APR *',
    '0 0 12 ? 9-12 *'
]
# for expr in expr_ls:
#     print(get_description(expr, options))

class FormatException(Exception):
    pass


class CronValidator(object):
    _expression = ''

    _days_map = {
        'SUN': 0,
        'MON': 1,
        'TUE': 2,
        'WED': 3,
        'THU': 4,
        'FRI': 5,
        'SAT': 6
    }

    _months_map = {
        'JAN': 1,
        'FEB': 2,
        'MAR': 3,
        'APR': 4,
        'MAY': 5,
        'JUN': 6,
        'JUL': 7,
        'AUG': 8,
        'SEP': 9,
        'OCT': 10,
        'NOV': 11,
        'DEC': 12
    }

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

    def validate_expression(self, expression_parts, expr_length):
        print('expression_parts ', expression_parts)
        """Initializes a new instance of the ExpressionParser class
        Args:
            expression_parts: 
            expr_length: 

        """

        if expr_length == 5:
            self.second_minute(expression_parts[1], 'Second and Minute')
            self.hour(expression_parts[2], 'Hour')
            self.dayofmonth(expression_parts[3], 'DayOfMonth')
            self.month(expression_parts[4], 'Month')
            self.dayofweek(expression_parts[5], 'DayOfWeek')
        elif expr_length == 6:
            self.second_minute(expression_parts[0], 'Second and Minute')
            self.second_minute(expression_parts[1], 'Second and Minute')
            self.hour(expression_parts[2], 'Hour')
            self.dayofmonth(expression_parts[3], 'DayOfMonth')
            self.month(expression_parts[4], 'Month')
            self.dayofweek(expression_parts[5], 'DayOfWeek')
        else:
            self.second_minute(expression_parts[0], 'Second and Minute')
            self.second_minute(expression_parts[1], 'Second and Minute')
            self.hour(expression_parts[2], 'Hour')
            self.dayofmonth(expression_parts[3], 'DayOfMonth')
            self.month(expression_parts[4], 'Month')
            self.dayofweek(expression_parts[5], 'DayOfWeek')
            self.year(expression_parts[6], 'Year')

    def second_minute(self, expr, prefix):
        mi, mx = (0, 59)
        if re.fullmatch("\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.fullmatch(r"\d{1,2}-\d{1,2}$", expr):
                print(f'n-n {expr}')
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr):
                print(f'n/n {expr}')
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                print(f'n-n/n {expr}')
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\*/\d{1,2}$", expr):
                print("*/n ", expr)
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr):
                print(f'n,n {expr}')
                limit = 60
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for n in expr_ls:
                        self.check_range(expr=n, mi=mi, mx=mx, prefix=prefix)

            elif '*' == expr:
                pass

            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)

        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def hour(self, expr, prefix):
        mi, mx = (0, 23)
        if re.fullmatch("\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.fullmatch(r"\d{1,2}-\d{1,2}$", expr):
                print(f'n-n {expr}')
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr):
                print(f'n/n {expr}')
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                print(f'n-n/n {expr}')
                parts = expr.split("/")
                fst_parts = expr_parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\*/\d{1,2}$", expr):
                print("*/n ", expr)
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr):
                print(f'n,n {expr}')
                limit = 24
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix, 24,
                                                                                                            len(limit))
                    raise FormatException(msg)
                else:
                    for n in expr_ls:
                        self.check_range(expr=n, mi=mi, mx=mx, prefix=prefix)

            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def dayofmonth(self, expr, prefix):
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
        mi, mx = (1, 31)
        if re.fullmatch("\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)
        elif re.search(r"[-*,/?]", expr):
            if '*' == expr:
                pass

            elif '?' == expr:
                pass

            elif re.fullmatch(r"\d{1,2}-\d{1,2}$", expr):
                print(f'n-n {expr}')
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr):
                print(f'n/n {expr}')
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                print(f'n-n/n {expr}')
                parts = expr.split("/")
                fst_parts = expr_parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\*/\d{1,2}$", expr):
                print("*/n ", expr)
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr):
                print(f'n,n {expr}')
                limit = 31
                expr_ls = expr.split(",")
                if len(expr_ls) > 31:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix, 31,
                                                                                                            len(
                                                                                                                expr_ls))
                    raise FormatException(msg)
                else:
                    for dayofmonth in expr_ls:
                        self.check_range(expr=dayofmonth, mi=mi, mx=mx, prefix=prefix)
            elif re.fullmatch(r"^(L|l)-(\d{1,2})$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "Illegal Expression Format '{0}'".format(expr)
                raise FormatException(msg)

        elif re.fullmatch(r"^(L|l)(W|w)?$", expr):
            pass

        elif re.fullmatch(r"^(\d{1,2})(w{1}|W{1})$", expr):
            self.check_range(expr=expr[:-1], mi=mi, mx=mx, prefix=prefix)

        else:
            msg = "({0}) Illegal Expression Format {1}".format(prefix, expr)
            raise FormatException(msg)

    def month(self, expr, prefix):
        mi, mx = (1, 12)
        if re.fullmatch("\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\D{3}", expr):
            matched_month = [m for m in self._cron_months.values() if expr == m]
            if len(matched_month) == 0:
                msg = "Invalid Month value '{}'".format(expr)
                raise FormatException(msg)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.fullmatch(r"\d{1,2}-\d{1,2}$", expr):
                print(f'n-n {expr}')
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\D{3}-\D{3}$", expr):
                print(f'str-str {expr}')
                parts = expr.split("-")
                cron_months = {v: k for (k, v) in self._cron_months.items()}
                st_not_exist = parts[0] not in cron_months
                ed_not_exist = parts[1] not in cron_months
                if st_not_exist or ed_not_exist:
                    msg = "Invalid Month value '{}'".format(expr)
                    raise FormatException(msg)
                self.compare_range(st=cron_months[parts[0]], ed=cron_months[parts[1]], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}/\d{1,2}$", expr):
                print(f'n/n {expr}')
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                print(f'n-n/n {expr}')
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=12, prefix=prefix)

            elif re.fullmatch(r"\*/\d{1,2}$", expr):
                print("*/n ", expr)
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=0, mx=12, prefix=prefix)

            elif re.fullmatch(r"^\d{1,2}(,\d{1,2})+", expr):
                print(f'n,n: {expr}')
                limit = 12
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for month in expr_ls:
                        self.check_range(expr=month, mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"^(\d{1,2}|\D{3})((,\d{1,2})+|(,\D{3})*)*", expr):
                print(f'n|str,n|str: {expr}')
                limit = 12
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    cron_months = {v: k for (k, v) in self._cron_months.items()}
                    for month in expr_ls:
                        print(f'month n|str {month} {isinstance(month, str)}')
                        month = cron_months[month] if len(month) == 3 else month
                        self.check_range(expr=month, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            print(f'Unknown match {expr}')
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def dayofweek(self, expr, prefix):
        """ DAY  of Week field
        # ? - * n sss
        # ? - n-n, sss-sss
        # ? - n/n -> */n
        # ? - /D{1,3},/D{1,3}
        # ? - nL
        # ? - n#n
        """
        mi, mx = (1, 7)

        if '*' == expr:
            pass

        elif '?' == expr:
            pass

        elif re.fullmatch("\d{1}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.fullmatch("\D{3}", expr):
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            if expr.upper() in cron_days:
                pass
            else:
                msg = "Invalid DayOfWeek value '{}'".format(expr)
                raise FormatException(msg)

        elif re.fullmatch(r"\d{1}/\d{1}$", expr):
            print(f'n/n {expr}')
            parts = expr.split("/")
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
            print(f'n-n/n {expr}')
            parts = expr.split("/")
            fst_parts = parts[0].split("-")
            self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
            self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.fullmatch(r"[*]/\d{1}$", expr):
            print(f'*/n {expr}')
            parts = expr.split("/")
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\d{1}-\d{1}$", expr):
            print(f'n-n {expr}')
            parts = expr.split("-")
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\D{3}-\D{3}$", expr):
            print(f'sss-sss {expr}')
            parts = expr.split("-")
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            try:
                st_day = cron_days[parts[0].upper()]
                ed_day = cron_days[parts[1].upper()]
            except KeyError:
                msg = "({0}) Invalid DayOfWeek value '{1}'".format(prefix, expr)
                raise FormatException(msg)
            self.compare_range(st=st_day, ed=ed_day, mi=mi, mx=mx, prefix=prefix, type='dow')

        elif re.fullmatch(r"^(\d{1}|\D{3})((,\d{1})+|(,\D{3})*)*", expr):
            print(f'n,n {expr}')
            limit = 7
            expr_ls = expr.split(",")
            if len(expr_ls) > limit:
                msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix, limit,
                                                                                                        len(expr_ls))
                raise FormatException(msg)
            else:
                cron_days = {v: k for (k, v) in self._cron_days.items()}
                for day in expr_ls:
                    day = cron_days[day.upper()] + 1 if len(day) == 3 else day  # syncronize by add 1 to cron_days index
                    self.check_range(expr=day, mi=mi, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\d{1}(l|L)", expr):
            print(f'nL {expr}')
            self.check_range(expr=expr[0], mi=mi, mx=mx, prefix=prefix)

        elif re.fullmatch(r"\d{1}#\d{1}", expr):
            print(f'n#n {expr}')
            parts = expr.split('#')
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=parts[1], mi=mi, mx=5, prefix=prefix, type='dow')
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def year(self, expr, prefix):
        mi, mx = (1970, 2099)
        if re.fullmatch("\d{4}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):

            if '*' == expr:
                pass

            elif re.fullmatch(r"\d{4}-\d{4}$", expr):
                print(f'n-n {expr}')
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\d{4}/\d{1,3}$", expr):
                print(f'n/n {expr}')
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=129, prefix=prefix)

            elif re.fullmatch(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                print(f'n-n/n {expr}')
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"\*/\d{1,3}$", expr):
                print("*/n ", expr)
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.fullmatch(r"^\d{4}(,\d{4})+", expr):
                print(f'n,n {expr}')
                limit = 84
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for year in expr_ls:
                        self.check_range(expr=year, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def check_range(self, type=None, **kwargs):
        prefix = kwargs["prefix"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        expr = kwargs["expr"]
        if int(expr) < mi or mx < int(expr):
            if type is None:
                msg = "{0} values must be between {1} and {2} but '{3}' is provided".format(prefix, mi, mx, expr)
            elif type == "interval":
                msg = "({0}) Accepted increment value range is {1}~{2} but '{3}' is provided".format(prefix, mi, mx,
                                                                                                     expr)
            elif type == 'dow':
                msg = "({0}) Accepted week value is {1}~{2} but '{3}' is provided".format(prefix, mi, mx, expr)
            raise FormatException(msg)
        else:
            pass

    def compare_range(self, type=None, **kwargs):
        prefix = kwargs["prefix"]
        st = kwargs["st"]
        ed = kwargs["ed"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        print(f'st {st}, ed {ed} {int(st) < int(ed)}')
        if int(st) > int(ed):
            if type is None:
                msg = "({0}) Invalid range '{1}-{2}'. Accepted range is {3}-{4}".format(prefix, st, ed, mi, mx)
            elif type == 'dow':
                msg = "({0}) Invalid range '{1}-{2}'. Accepted range is {3}-{4}".format(prefix, self._cron_days[st],
                                                                                        self._cron_days[ed], mi, mx)
            raise FormatException(msg)
