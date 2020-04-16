$(document).ready(function(){
    
    // Récupère la variable depart passée par python à l'initialisation de la page
    var state = $("#inittaquin").val()
    console.log("Engine started " + state);
    
    // un compteur du nombre de déplacements
    var nbclick = 0;
    // un booléen pour savoir si une animation est en cours 
    var lock = true;
    // Fonction qui met à jour l'état de la grille représentée par la chaîne des numéro
    function update(state, num){
        
        // Echange la position du 1 et du 9 dans la chaîne qui représente la grille
        //console.log(state.replace(/[19]/g, function($1) { return $1 === '1' ? '9' : '1' }));
        var regex = new RegExp("[" + num + "0]", "g");
        // Cette ligne construit l'expression régulière /[num9]/g pour num variant de 1 à 8
        return state.replace(regex, function($1) { return $1 === num ? '0' : num });
    };

    // Fonction qui détermine les coordonnées du coin haut gauche d'une tuile  
    function logposition(element){
        console.log(element.attr('id') + " top " + element.position().top + " left "+ element.position().left);
    };
    
    // Fonction qui renvoie les paramètres de direction pour l'animation d'une tuile
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
    
    // Fonction qui renvoie les paramètres de direction pour l'animation de la tuile vide
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
    
    // Fonction qui échange un élément avec la tuile vide
    function echange(element, direction, duree){
        var TL = gsap.timeline();
        TL
            .to(element, duree, getdir(direction), "+=0.5")
            .to($("#piece_0"), duree, oppositedir(direction), "-=0.5")  
    };
    
    // On écoute les click sur les tuiles (classe piece) et on détermine si l'élément est clickable
    $('div.piece').click(function(){
        
        // Récupère l'id de la pièce sur laquelle on clique
        console.log("You just clicked on "+ $(this).attr('id'))
               
        // Récupère le numéro de la tuile
        var numero = $(this).attr('id').charAt($(this).attr('id').length-1);
        
        // Récupère les coordonnées du coin haut gauche de la tuile
        var pos = $(this).position();
        
        var pos_top=pos.top;
        var pos_left=pos.left;
        //console.log("case cliquée à top "+ pos_top + " case cliquée à left "+ pos_left);
        
        // Récupère les coordonnées du coin haut gauche de la tuile vide        
        var tuilevidetop = $("#piece_0").position().top;
        var tuilevideleft = $("#piece_0").position().left;
        //console.log("case vide top "+ tuilevidetop + " case vide left "+ tuilevideleft);
        
        // Calcul de distance par rapport à la tuile vide
        var x=(tuilevideleft-pos_left);
        var y=(tuilevidetop-pos_top);
        var dist=Math.sqrt(x*x+y*y);
        //console.log("dist", dist);
        
        // Test sur la distance pour savoir si c'est clickable
        if (dist>Math.sqrt(80000)-1) {
            var clickable = false;
        }
        else {
            var clickable = true;
        }
        
        //Si le taquin est déjà résolu
        if(state == '012345678'){
            alert("I have already brought peace, freedom, justice, and security to my new empire");
        }
        
        // Si l'élément est clickable, on l'échange avec la tuile vide
        else if (clickable && dist!==0){
            console.log("This is a legal move");
            
            // Mise à jour du nombre de déplacements
            nbclick += 1;
            //console.log("nb de clicks", nbclick)
            $("#compteur").text("Déplacements effectués : " + nbclick);
            
            // On cherche dans quel sens bouger avant de faire l'échange
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
            console.log("Update "+ state);
            
            request = {"action": "mymove", "argument2": tuilevidedir};
            send_info('/action', request);
        }
        
        else {
            alert("This is not the tile you're looking for");
        }
    });
    
    function updateclickcount(loop) { 
        setTimeout(function() {
            nbclick += 1;
            $("#compteur").text("Déplacements effectués : " + nbclick);
        }, 1000 * loop); 
    } 

    
    // Fonction d'envoi de données au module python
    function send_info(receiver, to_send){
        $.ajax({
            type : 'GET',
            url : receiver,
            data : to_send,
            success : function(){console.log("Transmitting...");},
            error : function(){console.log("BSoD : Erreur fatale pendant la demande d'action " + Object.values(to_send)[0]);}
            })
            // On exécute cette fonction au retour
            // Plusieurs actions sont possibles au retour
            // Soit on affiche de l'aide
            // Soit on échange la position d'une tuile avec la case vide
            // Soit on anime pour accéder à l'état gagnant
            .done(function(data){               
                // Produit un dictionnaire à partir des données envoyées par python
                var returned = JSON.parse(data); 
                console.log("R2D2 sent back", Object(returned));
                //console.log("return data => clefs " + Object.keys(returned)[0] + " " + Object.keys(returned)[1]);
                //console.log("return data => valeurs " + Object.values(returned)[0] + " " + Object.values(returned)[1]);
                
                if (Object.values(returned)[1] == "beep-end"){
                    alert("I find your lack of faith disturbing");
                }
                
                else if (Object.values(returned)[0] == "help me Obi-wan Kenobi, you're my only hope" & state !='012345678'){
                    var nextmove = ""
                    for ( rang = 0; rang < 9; rang++){
                        // Tous les 3 caractères on place un retour à la ligne
                        if (rang % 3 == 0) {
                        // Remplace le 0 par un espace vide
                            if (Object.values(returned)[1][rang] == '0'){
                                nextmove = nextmove + '\n' + '  ';
                            }
                            else {
                                nextmove = nextmove + '\n' + Object.values(returned)[1][rang];
                            }
                        }
                        else{
                            if (Object.values(returned)[1][rang] == '0'){
                                nextmove = nextmove + '  ';
                            }
                            else {
                                nextmove = nextmove  + Object.values(returned)[1][rang];
                            }
                        }
                    }
                    alert("I have a good (not a bad one) feeling about this : "+ nextmove)
                
                }
                // Sinon c'est qu'il faut faire l'animation d'un déplacement    
                else if (Object.values(returned)[0] == "mymove"){
                    //console.log("swap of pieces done")
                    
                    setTimeout(function () {
                        if (state == '012345678') {
                            alert("You've just restored balance to the Force and brought peace to the Galaxy");
                        }
                    }, 1500);
                }
                
                // Sinon c'est qu'on a un algo de recherche qui a tourné et il faut animer la succession de déplacements vers l'état solution                   
                else if (Object.values(returned)[1] != "already done"){
                    var stringtoprocess = Object.values(returned)[1];
                    //Création d'une timeline pour l'animation
                    var solveTL = gsap.timeline();
                  
                    for (i = 0; i < stringtoprocess.length/2; i++){       
                        solveTL
                            .to($("#piece_" + stringtoprocess[2*i]), 0.5, getdir(stringtoprocess[2*i+1]), "+=0.5")
                            .to($("#piece_0"), 0.5, oppositedir(stringtoprocess[2*i+1]), "-=0.5")
                        
                        // Mise à jour du nombre de déplacements
                        updateclickcount(i);
                    }
                    state = '012345678';
                    //console.log("after animation", state)
                }
            })
    }
    
    // On écoute les clicks sur l'un des boutons de résolution automatique
    $(".btn").click(function(event){
        event.preventDefault();
        button_id = $(this).attr('id');
        //console.log("state au click", state)
        if (button_id == 'btn_helpme'){
            request = {"action":"help me Obi-wan Kenobi, you're my only hope", "argument2":state}
        }
        
        else {
            //console.log("id du bouton", button_id);
            searchmethod = button_id.slice(button_id.length - 7);
            request = {"action":searchmethod, "argument2":state};   
        }
        console.log("C3P0 sends", request);
        send_info('/action', request);
    });
    
    // Bouton pour remettre à 0 le compteur de déplacements
    $("#reset").click(function(event) {
            $("#compteur").text("Déplacements effectués : 0");
            nbclick = 0;
    });

});
