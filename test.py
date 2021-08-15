hits_textures = pygame.sprite.groupcollide(self.bullets_lst, self.texture_lst, False, False)
if hits_textures:
    for hit_tex in hits_textures:
        textcoords = [hits_textures[hit_tex][0].rect[0], hits_textures[hit_tex][0].rect[1]]
        for k,v in map.items():
            if (isinstance(v,list) and textcoords in v) or textcoords == v:
                if k == 'cementf' or k == 'cementv' or k == 'cementh':
                    pygame.sprite.groupcollide(self.bullets_lst, self.texture_lst, True, False)
                    break
                elif k == 'tree' or k == 'water':
                    pygame.sprite.groupcollide(self.bullets_lst, self.texture_lst, False, False)
                else:
                    pygame.sprite.groupcollide(self.bullets_lst, self.texture_lst, True, True)