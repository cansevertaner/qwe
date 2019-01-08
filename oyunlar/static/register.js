 function validate()
 {
      if( document.myForm.username.value == "" )
         {
            alert( "Lütfen isim girin!" );
            document.myForm.username.focus() ;
            return false;
         }
         if( document.myForm.email.value == "" )
         {
            alert( "Email adresi giriniz!" );
            document.myForm.email.focus() ;
            return false;
         }
         if( document.myForm.email.value != "" ) {
             var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
             if (!filter.test(document.myForm.email.value)) {
                 alert('Lütfen geçerli mail adresi giriniz!');
                 document.myForm.email.focus();
                 return false;
             }
         }
         if( document.myForm.password.value == "")
         {
            alert( "Şifreyi boş girmeyiniz" );
            document.myForm.password.focus() ;
            return false;
         }
         if( document.myForm.confirm.value == "" )
         {
            alert( "Lütfen onaylama şifresini girin!" );
            document.myForm.confirm.focus() ;
            return false;
         }
          if( document.myForm.confirm.value != document.myForm.password.value  )
         {
            alert( "Şifreler uyuşmamaktadır!" );
            document.myForm.password.focus() ;
            return false;
         }
         return( true );
 }