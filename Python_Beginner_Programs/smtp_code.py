import smtplib

my_Email = "kollichintu@gmail.com"
password_App = "vvzqkuudqezabqfz"

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_Email, password=password_App)
    connection.sendmail(
        from_addr=my_Email, 
        to_addrs="laxman.kolli@aggne.com", 
        msg="Subject:Test Mail\n\n This is the body of my test Email."
 )

    
