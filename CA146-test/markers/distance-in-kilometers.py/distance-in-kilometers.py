#!/usr/bin/env python3

# Converting from metres to kilometers is trivial, we just divide by 1000.
#
# The trick here, however, is the requirement that we don't always round down,
# rather we round to the nearest kilometer.
#
# It turns out that there is a very simple trick that we can use to achieve
# this effect: we simply add 500 meters to the original number.
#
# Consider:
#
#   m              m + 500        kilometers
#   ------------------------------------------
#   7000 meters -> 7500 meters -> 7 kilometers
#   7499 meters -> 7999 meters -> 7 kilometers
#   7500 meters -> 8000 meters -> 8 kilometers
#   7501 meters -> 8001 meters -> 8 kilometers

m = int(input())

print((m + 500) // 1000)
