import re
from Exception import FormatException


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

    def __init__(self, expression):
        pass

    def validate_expression(self, expression_parts, expr_length):
        """Validation for each expression fields
        Args:
            expression_parts: expression list
            expr_length: length of the list
        """

        """
        Apply different index for varying length of the expression parts as it is mutated by parse().
        Does not validate the case for having both DOW,DOM value because it is already causing exception.
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
        """ sec/min expressions (n : Number, s: String)
        *
        nn (1~59)
        nn-nn
        nn/nn
        nn-nn/nn
        */nn
        nn,nn,nn (Maximum 24 elements)
        """
        mi, mx = (0, 59)
        if re.match(r"\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.match(r"\d{1,2}-\d{1,2}$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\*/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"^(\d{1,2}|\d{1,2}-\d{1,2})(,\d{1,2}|,\d{1,2}-\d{1,2})+$", expr):
                limit = 60
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for n in expr_ls:
                        if '-' in n:
                            parts = n.split("-")
                            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)
                        else:
                            self.check_range(expr=n, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)

        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def hour(self, expr, prefix):
        """ hour expressions (n : Number, s: String)
        *
        nn (1~23)
        nn-nn
        nn/nn
        nn-nn/nn
        */nn
        nn,nn,nn (Maximum 24 elements)
        """
        mi, mx = (0, 23)
        if re.match(r"\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.match(r"\d{1,2}-\d{1,2}$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\*/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"^(\d{1,2}|\d{1,2}-\d{1,2})(,\d{1,2}|,\d{1,2}-\d{1,2})+$", expr):
                limit = 24
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix, 24,
                                                                                                            len(limit))
                    raise FormatException(msg)
                else:
                    for n in expr_ls:
                        if '-' in n:
                            parts = n.split("-")
                            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)
                        else:
                            self.check_range(expr=n, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def dayofmonth(self, expr, prefix):
        """ DAYOfMonth expressions (n : Number, s: String)
        *
        ?
        nn (1~31)
        nn-nn
        nn/nn
        nn-nn/nn
        */nn
        nn,nn,nn (Maximum 31 elements)
        L-nn
        LW
        nW
        """
        mi, mx = (1, 31)
        if re.match(r"\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)
        elif re.search(r"[-*,/?]", expr):
            if '*' == expr:
                pass

            elif '?' == expr:
                pass

            elif re.match(r"\d{1,2}-\d{1,2}$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.match(r"\*/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.match(r"^\d{1,2}(,\d{1,2})+$", expr):
                limit = 31
                expr_ls = expr.split(",")
                if len(expr_ls) > 31:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for dayofmonth in expr_ls:
                        self.check_range(expr=dayofmonth, mi=mi, mx=mx, prefix=prefix)
            elif re.match(r"^(L|l)-(\d{1,2})$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "Illegal Expression Format '{0}'".format(expr)
                raise FormatException(msg)

        elif re.match(r"^(L|l)(W|w)?$", expr):
            pass

        elif re.match(r"^(W|w)(L|l)?$", expr):
            pass

        elif re.match(r"^(\d{1,2})(w{1}|W{1})$", expr):
            self.check_range(expr=expr[:-1], mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"^(w{1}|W{1})(\d{1,2})$", expr):
            self.check_range(expr=expr[1:], mi=mi, mx=mx, prefix=prefix)

        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def month(self, expr, prefix):
        """ month expressions (n : Number, s: String)
        *
        nn (1~12)
        sss (JAN~DEC)
        nn-nn
        sss-sss
        nn/nn
        nn-nn/nn
        */nn
        nn,nn,nn,nn-nn,sss-sss (Maximum 12 elements)
        """
        mi, mx = (1, 12)
        if re.match(r"\d{1,2}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"\D{3}$", expr):
            matched_month = [m for m in self._cron_months.values() if expr == m]
            if len(matched_month) == 0:
                msg = "Invalid Month value '{}'".format(expr)
                raise FormatException(msg)

        elif re.search(r"[-*,/]", expr):
            if '*' == expr:
                pass

            elif re.match(r"\d{1,2}-\d{1,2}$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\D{3}-\D{3}$", expr):
                parts = expr.split("-")
                cron_months = {v: k for (k, v) in self._cron_months.items()}
                st_not_exist = parts[0] not in cron_months
                ed_not_exist = parts[1] not in cron_months
                if st_not_exist or ed_not_exist:
                    msg = "Invalid Month value '{}'".format(expr)
                    raise FormatException(msg)
                self.compare_range(st=cron_months[parts[0]], ed=cron_months[parts[1]], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

            elif re.match(r"\d{1,2}-\d{1,2}/\d{1,2}$", expr):
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=12, prefix=prefix)

            elif re.match(r"\*/\d{1,2}$", expr):
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=0, mx=12, prefix=prefix)

            elif re.match(r"^\d{1,2}(,\d{1,2})+$", expr):
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

            elif re.match(r"^((\d{1,2}|\D{3})|(\D{3}-\D{3})|(\d{1,2}-\d{1,2}))((,\d{1,2})+"
                          r"|(,\D{3})*|(,\d{1,2}-\d{1,2})*|(,\D{3}-\D{3})*)*$", expr):
                """
                    1st Capture group : digit{1~2}|nondigit{3}|nondigit{3}-nondigit{3}|digit{3}-digit{3}
                    2nd Capture group : same with 1st capture group but repeated.
                """
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
                        if '-' in month:
                            parts = month.split("-")
                            if len(parts[0]) == 3:
                                self.check_range(expr=cron_months[parts[0].upper()], mi=mi, mx=mx, prefix=prefix)
                                self.check_range(expr=cron_months[parts[1].upper()], mi=mi, mx=mx, prefix=prefix)
                            else:
                                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)
                        else:
                            month = cron_months[month.upper()] if len(month) == 3 else month
                            self.check_range(expr=month, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def dayofweek(self, expr, prefix):
        """ DAYOfWeek expressions (n : Number, s: String)
        *
        ?
        n (0~7) - 0 and 7 used interchangeable as Sunday
        sss (SUN~SAT)
        n/n
        n-n/n
        */n
        n-n
        sss-sss
        n|sss,n|sss,n|sss,n-n,sss-sss (maximum 7 elements)

        nL
        n#n
        """
        mi, mx = (0, 7)

        if '*' == expr:
            pass

        elif '?' == expr:
            pass

        elif re.match(r"\d{1}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"\D{3}$", expr):
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            if expr.upper() in cron_days:
                pass
            else:
                msg = "Invalid value '{}'".format(expr)
                raise FormatException(msg)

        elif re.match(r"\d{1}/\d{1}$", expr):
            parts = expr.split("/")
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.match(r"\d{1}-\d{1}/\d{1}$", expr):
            parts = expr.split("/")
            fst_parts = parts[0].split("-")
            self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
            self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.match(r"[*]/\d{1}$", expr):
            parts = expr.split("/")
            self.check_range('interval', expr=parts[1], mi=0, mx=mx, prefix=prefix)

        elif re.match(r"\d{1}-\d{1}$", expr):
            parts = expr.split("-")
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"\D{3}-\D{3}$", expr):
            parts = expr.split("-")
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            try:
                st_day = cron_days[parts[0].upper()]
                ed_day = cron_days[parts[1].upper()]
            except KeyError:
                msg = "({0}) Invalid value '{1}'".format(prefix, expr)
                raise FormatException(msg)
            self.compare_range(st=st_day, ed=ed_day, mi=mi, mx=mx, prefix=prefix, type='dow')

        elif re.match(r"^((\d{1}|\D{3})|(\D{3}-\D{3})|(\d{1}-\d{1}))"
                      r"((,\d{1})+|(,\D{3})*|(,\d{1}-\d{1})*|(,\D{3}-\D{3})*)*$", expr):
            limit = 7
            expr_ls = expr.split(",")
            if len(expr_ls) > limit:
                msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix, limit,
                                                                                                        len(expr_ls))
                raise FormatException(msg)
            else:
                cron_days = {v: k for (k, v) in self._cron_days.items()}
                for day in expr_ls:
                    if '-' in day:
                        parts = day.split("-")
                        if len(parts[0]) == 3:
                            self.check_range(expr=cron_days[parts[0].upper()], mi=mi, mx=mx, prefix=prefix)
                            self.check_range(expr=cron_days[parts[1].upper()], mi=mi, mx=mx, prefix=prefix)
                        else:
                            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)
                    else:
                        # syncronize by add 1 to cron_days index
                        day = cron_days[day.upper()] + 1 if len(day) == 3 else day
                        self.check_range(expr=day, mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"\d{1}(l|L)$", expr):
            parts = expr.upper().split('L')
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)

        elif re.match(r"\d{1}#\d{1}$", expr):
            parts = expr.split('#')
            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
            self.check_range(expr=parts[1], mi=mi, mx=5, prefix=prefix, type='dow')
        elif re.match(r"\D{3}#\d{1}$", expr):
            parts = expr.split('#')
            cron_days = {v: k for (k, v) in self._cron_days.items()}
            try:
                st_day = cron_days[parts[0].upper()]
            except KeyError:
                msg = "({0}) Invalid value '{1}'".format(prefix, expr)
                raise FormatException(msg)
            self.check_range(expr=parts[1], mi=mi, mx=5, prefix=prefix, type='dow')
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def year(self, expr, prefix):
        """ Year - valid expression (n : Number)
        *
        nnnn(1970~2099) - 4 digits number
        nnnn-nnnn(1970~2099)
        nnnn/nnn(0~129)
        */nnn(0~129)
        nnnn,nnnn,nnnn(1970~2099) - maximum 86 elements
        """
        mi, mx = (1970, 2099)
        if re.match(r"\d{4}$", expr):
            self.check_range(expr=expr, mi=mi, mx=mx, prefix=prefix)

        elif re.search(r"[-*,/]", expr):

            if '*' == expr:
                pass

            elif re.match(r"\d{4}-\d{4}$", expr):
                parts = expr.split("-")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)

            elif re.match(r"\d{4}/\d{1,3}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=129, prefix=prefix)

            elif re.match(r"\d{4}-\d{4}/\d{1,3}$", expr):
                parts = expr.split("/")
                fst_parts = parts[0].split("-")
                self.check_range(expr=fst_parts[0], mi=mi, mx=mx, prefix=prefix)
                self.check_range(expr=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.compare_range(st=fst_parts[0], ed=fst_parts[1], mi=mi, mx=mx, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=129, prefix=prefix)

            elif re.match(r"\*/\d{1,3}$", expr):
                parts = expr.split("/")
                self.check_range('interval', expr=parts[1], mi=0, mx=129, prefix=prefix)

            elif re.match(r"\d{1}/\d{1,3}$", expr):
                parts = expr.split("/")
                self.check_range(expr=parts[0], mi=0, mx=129, prefix=prefix)
                self.check_range('interval', expr=parts[1], mi=0, mx=129, prefix=prefix)

            elif re.match(r"^(\d{4}|\d{4}-\d{4})(,\d{4}|,\d{4}-\d{4})+$", expr):
                limit = 84
                expr_ls = expr.split(",")
                if len(expr_ls) > limit:
                    msg = "({0}) Exceeded maximum number({1}) of specified value. '{2}' is provided".format(prefix,
                                                                                                            limit, len(
                            expr_ls))
                    raise FormatException(msg)
                else:
                    for year in expr_ls:
                        if '-' in year:
                            parts = year.split("-")
                            self.check_range(expr=parts[0], mi=mi, mx=mx, prefix=prefix)
                            self.check_range(expr=parts[1], mi=mi, mx=mx, prefix=prefix)
                            self.compare_range(st=parts[0], ed=parts[1], mi=mi, mx=mx, prefix=prefix)
                        else:
                            self.check_range(expr=year, mi=mi, mx=mx, prefix=prefix)
            else:
                msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
                raise FormatException(msg)
        else:
            msg = "({0}) Illegal Expression Format '{1}'".format(prefix, expr)
            raise FormatException(msg)

    def check_range(self, type=None, **kwargs):
        """
        check if expression value within range of specified limit
        """
        prefix = kwargs["prefix"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        expr = kwargs["expr"]
        if int(expr) < mi or mx < int(expr):
            if type is None:
                msg = "{0} values must be between {1} and {2} but '{3}' is provided".format(prefix, mi, mx, expr)
            elif type == "interval":
                msg = "({0}) Accepted increment value range is {1}~{2} but '{3}' is provided".format(prefix,
                                                                                                     mi, mx, expr)
            elif type == 'dow':
                msg = "({0}) Accepted week value is {1}~{2} but '{3}' is provided".format(prefix, mi, mx, expr)
            raise FormatException(msg)
        else:
            pass

    def compare_range(self, type=None, **kwargs):
        """ check 2 expression values size
        does not allow {st} value to be greater than {ed} value
        """
        prefix = kwargs["prefix"]
        st = kwargs["st"]
        ed = kwargs["ed"]
        mi = kwargs["mi"]
        mx = kwargs["mx"]
        if int(st) > int(ed):
            if type is None:
                msg = "({0}) Invalid range '{1}-{2}'. Accepted range is {3}-{4}".format(prefix, st, ed, mi, mx)
            elif type == 'dow':
                msg = "({0}) Invalid range '{1}-{2}'. Accepted range is {3}-{4}".format(prefix,
                                                                                        self._cron_days[st],
                                                                                        self._cron_days[ed], mi, mx)
            raise FormatException(msg)
