$(document).ready(function(){
    
    //Récupère la variable depart passée par python à l'initialisation de la page
    var state = $("#inittaquin").val()
    console.log("départ " + state);
    
    //un booléen pour savoir si une animation est en cours 
    var lock = true;
    //Fonction qui met à jour l'état de la grille représentée par la chaîne des numéro
    function update(state, num){
        
        //Echange la position du 1 et du 9 dans la chaîne qui représente la grille
        //console.log(state.replace(/[19]/g, function($1) { return $1 === '1' ? '9' : '1' }));
        var regex = new RegExp("[" + num + "0]", "g");
        // Cette ligne construit l'expression régulière /[num9]/g pour num variant de 1 à 8
        return state.replace(regex, function($1) { return $1 === num ? '0' : num });
    };

    //Fonction qui détermine les coordonnées du coin haut gauche d'une tuile  
    function logposition(element){
        console.log(element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
    };
    
    //Fonction qui renvoie les paramètres de direction pour l'animation d'une tuile
    function getdir(chaine){
        var param=""
        if(chaine=="G"){
            param ={x:"-=200"}
        }
        if(chaine=="D"){
            param ={x:"+=200"}
        }
        if(chaine=="H"){
            param ={y:"-=200"}
        }
        if(chaine=="B"){
            param ={y:"+=200"}
        }
        return param
    };
    
    //Fonction qui renvoie les paramètres de direction pour l'animation de la tuile vide
    function oppositedir(chaine){
        var param=""
        if(chaine=="G"){
            param ={x:"+=200"}
        }
        if(chaine=="D"){
            param ={x:"-=200"}
        }
        if(chaine=="H"){
            param ={y:"+=200"}
        }
        if(chaine=="B"){
            param ={y:"-=200"}
        }
        return param
    };
    
    //Fonction qui échange un élément avec la tuile vide
    function echange(element, direction, duree){
        var TL = gsap.timeline();
        TL
            .to(element, duree, getdir(direction), "+=0.5")
            .to($("#piece_0"), duree, oppositedir(direction), "-=0.5")  
    
        //console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
        
        //Equivalent dans l'ancienne version à 
        // gsap.to(element, {duration: 1, x: "-=200", onComplete:function(){
        //            console.log("after move " + element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
        //            }   
    };
    
    
    
    var nbclick = 0;
    
    //On écoute les click sur les tuiles (classe piece) et on détermine si l'élément est clickable
    $('div.piece').click(function(){
        
        //Récupère l'id de la pièce sur laquelle on clique
        console.log("On vient de clicker sur "+ $(this).attr('id'))
               
        //Récupération du numéro de la piece
        var numero = $(this).attr('id').charAt($(this).attr('id').length-1);
        
        //Récupère les coordonnées du coin haut gauche de la pièce
        var pos = $(this).position();
        
        var pos_top=pos.top;
        var pos_left=pos.left;
        //console.log("case cliquée à top "+ pos_top + " case cliquée à left "+ pos_left);
        
        //Récupère les coordonnées du coin haut gauche de la tuile vide        
        //var tuilevidetop = ajuste_top($("#piece_9"));
        var tuilevidetop = $("#piece_0").position().top;
        var tuilevideleft = $("#piece_0").position().left;
        //console.log("case vide top "+ tuilevidetop + " case vide left "+ tuilevideleft);
        
        //Calcul de distance par rapport à la tuile vide
        var x=(tuilevideleft-pos_left);
        var y=(tuilevidetop-pos_top);
        var dist=Math.sqrt(x*x+y*y);
        //console.log("dist", dist);
        
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
            
            //Mise à jour du nombre de clicks
            nbclick += 1;
            //console.log("nb de clicks", nbclick)
            $("#compteur").text("Déplacements effectués : " + nbclick);
            
            //On cherche dans quel sens bouger avant de faire l'échange
            if (pos_left == tuilevideleft && pos_top < tuilevidetop){
                echange($(this),"B", 0.5);     
                var tuilevidedir = "H";   
            }
            else if (pos_top > tuilevidetop){
                echange($(this),"H", 0.5);
                var tuilevidedir = "B";
            }
            if (pos_top == tuilevidetop && pos_left < tuilevideleft){
                echange($(this),"D", 0.5); 
                var tuilevidedir = "G";       
            }
            else if (pos_left > tuilevideleft){
                echange($(this),"G", 0.5);
                var tuilevidedir = "D";
            }
            //Mise à jour de la chaîne représentant l'état (équivalent à Etat(untaquin) dans la partie python)
            state = update(state, numero);
            console.log("update "+ state);
            
            request = {"action": "mymove", "argument2": tuilevidedir};
            send_info('/action', request);
        }
        else {
            alert("Vous ne pouvez pas déplacer cette tuile");
        }
        });
    
    //Fonction d'envoi de données au module python
    function send_info(receiver, to_send){
        $.ajax({
            type : 'GET',
            url : receiver,
            data : to_send,
            success : function(){console.log("Retour python effectué");},
            error : function(){console.log("BSoD : Erreur fatale pendant la demande d'action " + Object.values(to_send)[0]);}
            })
            // On exécute cette fonction au retour
            // Pour l'instant, on montre un mélange des tuiles via une animation
            .done(function(data){               
                // produit un dictionnaire à partir des données envoyées par python
                var returned = JSON.parse(data); 
                console.log("return data => clefs " + Object.keys(returned)[0] + " " + Object.keys(returned)[1]);
                console.log("return data => valeurs " + Object.values(returned)[0] + " " + Object.values(returned)[1]);
                
                if (Object.values(returned)[0] == "giveup1"){
                    var stringtoprocess = Object.values(returned)[1];
                    //Création d'une timeline pour l'animation
                    var solveTL = gsap.timeline();
                    
                    for (i = 0; i < stringtoprocess.length/2; i++){
                        solveTL
                            .to($("#piece_" + stringtoprocess[2*i]), 0.5, getdir(stringtoprocess[2*i+1]), "+=0.5")
                            .to($("#piece_0"), 0.5, oppositedir(stringtoprocess[2*i+1]), "-=0.5")
                
                    }
                    state = '012345678';
                    console.log("après animation DLS " + state)
                }
                
                if (Object.values(returned)[0] == "giveup2"){
                    var stringtoprocess = Object.values(returned)[1];
                    //Création d'une timeline pour l'animation
                    var solveTL = gsap.timeline();
                    
                    for (i = 0; i < stringtoprocess.length/2; i++){
                        solveTL
                            .to($("#piece_" + stringtoprocess[2*i]), 0.5, getdir(stringtoprocess[2*i+1]), "+=0.5")
                            .to($("#piece_0"), 0.5, oppositedir(stringtoprocess[2*i+1]), "-=0.5")
                
                    }
                    state = '012345678';
                    console.log("after IDA*", state)
                }
                
                if (Object.values(returned)[0] == "mymove"){
                    console.log("swap of pieces done")
                    
                    setTimeout(function () {
                        if (state == '012345678') {
                            alert('Congratulations on solving the puzzle !');
                        }
                    }, 1500);
                    
                }
            })
    }
    
    //On écoute le click sur le bouton qui actionne la solution via BFS+DFS
    $("#btn_giveup1").click(function(event){
        event.preventDefault();
        button_id = $(this).attr('id');
        console.log("state", state);
        if (button_id == "btn_giveup1"){
                request = {"action":"giveup1", "argument2":state};
                send_info('/action', request);         
        }
    });
    
    
    //On écoute le click sur le bouton qui actionne la solution via IDA*
    $("#btn_giveup2").click(function(event){
        event.preventDefault();
        button_id = $(this).attr('id');
        console.log("state ", state);
        if (button_id == "btn_giveup2"){
                request = {"action":"giveup2", "argument2":state};
                send_info('/action', request);         
        }
    });

});
