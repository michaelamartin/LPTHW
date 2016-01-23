from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        # prints out last scene
        current_scene.enter()
        
class Death(Scene):

    death_scenarios = [
                                        "Nice job.  You are dead.",
                                        "Learn to shoot!  You are dead.",
                                        "Looks like you really screwed the pooch!  You are dead.",
                                        "Let's try this again.  You are dead.",
                                        "l2play.  You are dead.",
                                        "Think before you type.  You are dead.",
    ]                                     

    def enter(self):
        print Death.death_scenarios[randint(0, len(self.death_scenarios)-1)]
        exit(1)
        
class Vault101(Scene):

    def enter(self):
        print "The year is 2277, 200 years after the bombs dropped.  You"
        print "and your family reside safely below ground in Vault 101."
        print "Your father has disapeared.  Where do you go first?"
        print "You can either search Butche's Room (leader of the"
        print "Tunnel Snakes) or leave the vault and enter the wasteland."
        print """Type 1 to search Butch's room or 2 to enter the wasteland"""
        
        action = raw_input("> ")
        
        if action == "1":
            return 'butchs_room'    
        
        elif action == "2":
            return 'wasteland'       
            
        else:
            print "That is not a choice."
            return 'vault101'         
        
class ButchsRoom(Scene):

    def enter(self):
        print "You enter Butch's room.  Butch is standing at his"
        print "mother's vanity combing his hair and talking to"
        print "himself.  He quickly turns around as he hears you"
        print """approach.  He grins when he notices its you."""
        print """He says "Hey!  Just the man I wanted to see.  I"""
        print """I wanna show you somethin'.  Follow me." """
        print "You notice Butch is eyeing your new Pipboy."
        print "The whole situation is a little fishy.  What do you do?"
        print """Type 1 to follow Butch or you may choose to ignore his request"""
        print """ and type 2 to enter the wasteland"""
        
        action = raw_input(">")
        
        if action == "1":
            return 'tunnel_snake_room'    
        
        elif action == "2":
            return 'wasteland'     
            
        else:
            print "That is not a choice."
            return 'butchs_room'        
            
class TunnelSnakeRoom(Scene):
    
    def enter(self):
        print "Butch takes you down to an old supply room which is no longer in use."
        print "Out of the shadows come the silhouettes of three other young men."
        print "As they get closer you notice that they are Butch's friends -- Tunnel"
        print "Snakes.  Butch grabs a hold of your arms while the others beat you"
        print "senselessly.  They remove your Pipboy from your limp corpse."
        print "Why did you trust him again?"
        return 'death'
        
class Wasteland(Scene):

    def enter(self):
        print "Congratulations.  You have left the vault and begun your journey."
        print "to find your father.  Many hardships are ahead of you.  Just make"
        print "sure to watch out for deathclaws."
        return 'finished'      
        
class Finished(Scene):

    def enter(self):
        print "That's it! You won.  Good job."
        return 'finished'
       
class Map(Scene):

    scenes = {
        'vault_101' : Vault101(),
        'butchs_room' : ButchsRoom(),
        'tunnel_snake_room' : TunnelSnakeRoom(),
        'wasteland' : Wasteland(),
        'death' : Death(),
        'finished' : Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('vault_101')
a_game = Engine(a_map)
a_game.play()
