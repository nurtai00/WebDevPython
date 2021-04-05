st = input()
for i in st[:].split():
    st = st.replace(i, i.capitalize())
print(st)