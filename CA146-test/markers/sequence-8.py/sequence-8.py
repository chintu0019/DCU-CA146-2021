#!/usr/bin/env python3

x = -x + (x % 2) * 2 - 1
#        |     |   |   |
#        -- A --   |   |
#        |         |   |
#        ---- B ----   |
#        |             |
#        ------ C -----|
#
# A will be 0 or 1.
#
# B is (A * 2), so B will be 0 or 2.
#
# C is (B - 1), so C will be -1 or 1.
