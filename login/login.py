import kerbtest

kerb = kerbtest.kerberos()
usrnam = raw_input("Please Enter Username: ")

token = kerb.has_kerberos_ticket(usrnam)

print token

