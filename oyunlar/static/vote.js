$(document).ready(function(){
$('#add_vote').on('click',function (event) {
        $.ajax({
            url:$("#up_vote").attr('data-href'),
            type:'POST',
            dataType:'json',
            data:{
                user : $(this).attr('data-user-id'),
                soru_no: $(this).attr('data-game-id'),
                value_sts:$(this).attr('value_sts'),
                csrfmiddlewaretoken: csrf,
            }
        }).done(function (response) {

            $('#vote-count').html(response.vote);
            $('#card').html(response.yildiz);

        });
    })
$('#add_vote_neg').on('click',function (event) {
        $.ajax({
            url:$("#up_vote").attr('data-href'),
            type:'POST',
            dataType:'json',
            data:{
                user : $(this).attr('data-user-id'),
                soru_no: $(this).attr('data-game-id'),
                value_sts:$(this).attr('value_sts'),
                csrfmiddlewaretoken: csrf,
            }
        }).done(function (response) {
            $('#vote-count').html(response.vote);


        });

    })
});
