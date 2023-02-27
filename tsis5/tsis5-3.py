import re
patt=r"[a-z]_[a-z]"
txt="aa_b_c_v_d_gghghdd_f_g"
x=re.findall(patt, txt)
print(x)