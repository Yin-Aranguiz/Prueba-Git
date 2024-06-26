#

import re
texto = 'abc123'
texto2 = 'abc'
condicion = r'\w+'
cumple = re.search(condicion,texto)
print(cumple)
