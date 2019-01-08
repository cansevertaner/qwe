 function validate()
 {
      if( document.myForm.username.value == "" )
         {
            alert( "Lütfen kullanıcı adını girin!" );
            document.myForm.username.focus() ;
            return false;
         }
         if( document.myForm.password.value == "")
         {
            alert( "Şifre alanını boş bırakmayınız" );
            document.myForm.password.focus() ;
            return false;
         }
         return( true );
 }