from log import LogPrintMixin, LogFileMixin

lp = LogPrintMixin()
lp.log_error('Qualquer coisa')
lp.log_success('Que legal')
lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_success('Que legal')


