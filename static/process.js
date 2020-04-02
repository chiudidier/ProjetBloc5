$(document).ready(function(){
    /*
    //Ajuste la valeur position().top d'un élément
    function ajuste_top(element){
    var top=0;
        if (element.position().top>400) {
            top=400;
        }
        else if (element.position().top>200) {
            top=200;
        }  
    return top;
    };
    */
    
    function logposition(element){
        console.log(element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
    };
    
    function bouge(element, direction){
        if(direction=="G"){
            gsap.to(element, {duration: 1, x: "-=200", onComplete:function(){
                console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
                }
            });      
        }
        if(direction=="D"){
            gsap.to(element, {duration: 1, x: "+=200", onComplete:function(){
                console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
                }
            });      
        }
        if(direction=="H"){
            gsap.to(element, {duration: 1, y: "-=200", onComplete:function(){
                console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
                }
            });      
        }
        if(direction=="B"){
            gsap.to(element, {duration: 1, y: "+=200", onComplete:function(){
                console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
                }
            });      
        }
        
    };
    
    //Détermine si l'élément est clickable
    $('div.piece').click(function(){
        //Récupère l'id de la pièce sur laquelle on clique
        console.log("On vient de clicker sur "+ $(this).attr('id'))
        logposition($(this));
        logposition($('#piece_9'));       
        //Récupère les coordonnées du coin haut gauche de la pièce
        var pos = $(this).position();
        
        //pos_top=ajuste_top($(this));
        var pos_top=pos.top;
        var pos_left=pos.left;
        //console.log("case cliquée à top "+ pos_top + " case cliquée à left "+ pos_left);
        
        //Récupère les coordonnées du coin haut gauche de la tuile vide        
        //var tuilevidetop = ajuste_top($("#piece_9"));
        var tuilevidetop = $("#piece_9").position().top;
        var tuilevideleft = $("#piece_9").position().left;
        //console.log("case vide top "+ tuilevidetop + " case vide left "+ tuilevideleft);
        
        //Calcul de distance par rapport à la tuile vide
        var x=(tuilevideleft-pos_left);
        var y=(tuilevidetop-pos_top);
        var dist=Math.sqrt(x*x+y*y);
        console.log("dist", dist);
        
        //Test sur la distance pour savoir si c'est clickable
        if (dist>Math.sqrt(80000)-1) {
            var clickable = false;
        }
        else {
            var clickable = true;
        }
        
        //Si l'élément est clickable, on l'échange avec la tuile vide
        if (clickable && dist!==0){
            console.log("mouvement autorisé");
            
            //On cherche dans quel sens bouger
            if (pos_left == tuilevideleft && pos_top < tuilevidetop){
                //console.log($(this).attr('id') + " doit descendre et tuilevide doit monter");
                bouge($(this),"B");        
                bouge($('#piece_9'), "H");
                
            }
            else if (pos_top > tuilevidetop){
                //console.log($(this).attr('id') + " doit monter et tuilevide doit descendre");
                bouge($(this),"H");
                bouge($('#piece_9'), "B");

            }
            if (pos_top == tuilevidetop && pos_left < tuilevideleft){
                //console.log($(this).attr('id') + " doit aller à droite et tuilevide doit aller à gauche");
                bouge($(this),"D");        
                bouge($('#piece_9'), "G");
                
            }
            else if (pos_left > tuilevideleft){
                //console.log($(this).attr('id') + " doit aller à gauche et tuilevide doit aller à droite");
                bouge($(this),"G");
                bouge($('#piece_9'), "D");

            }
        }
        else {
            alert("Vous ne pouvez pas déplacer cette tuile");
        }
        });

});
