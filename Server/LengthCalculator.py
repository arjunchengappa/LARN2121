from math import sqrt

def calculate_len(p1,p2):
    dist=sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return dist
class Lenghts:
    def __init__(self):
        self.left_mouth_corner_jaw={"p1":54,"p2":8,"dist":0}
        self.right_mouth_corner_jaw={"p1":48,"p2":8,"dist":0}
        self.jaw_right_left={"p1":33,"p2":8,"dist":0}
        self.eye_left_up_down={"p1":43,"p2":47,"dist":0}
        self.eye_right_up_down={"p1":38,"p2":40,"dist":0}
        self.left_eye_corner_eyebrow={"p1":42,"p2":27,"dist":0}
        self.right_eye_corner_eyebrow={"p1":39,"p2":27,"dist":0}
        self.left_eye_nose={"p1":35,"p2":42,"dist":0}
        self.right_eye_nose={"p1":39,"p2":31,"dist":0}
        self.left_eyebrow_nose={"p1":27,"p2":22,"dist":0}
        self.right_eyebrow_nose={"p1":21,"p2":27,"dist":0}
        self.right_eye_length={"p1":36,"p2":39,"dist":0}
        self.left_eye_length={"p1":42,"p2":45,"dist":0}
        self.left_mouth_jaw_ratio=1
        self.right_mouth_jaw_ratio=1
        self.right_eyebrow_nose_ratio=1
        self.left_eyebrow_nose_ratio=1
        self.left_eye_open_ratio=1
        self.right_eye_open_ratio=1
    def update_len(self,coords):
        self.left_mouth_corner_jaw['dist']=calculate_len(coords[self.left_mouth_corner_jaw['p1']],coords[self.left_mouth_corner_jaw['p2']])
        self.right_mouth_corner_jaw['dist']=calculate_len(coords[self.right_mouth_corner_jaw['p1']],coords[self.right_mouth_corner_jaw['p2']])
        self.jaw_right_left['dist']=calculate_len(coords[self.jaw_right_left['p1']],coords[self.jaw_right_left['p2']])
        self.eye_left_up_down['dist']=calculate_len(coords[self.eye_left_up_down['p1']],coords[self.eye_left_up_down['p2']])
        self.eye_right_up_down['dist']=calculate_len(coords[self.eye_right_up_down['p1']],coords[self.eye_right_up_down['p2']])
        self.left_eye_corner_eyebrow['dist']=calculate_len(coords[self.left_eye_corner_eyebrow['p1']],coords[self.left_eye_corner_eyebrow['p2']])
        self.right_eye_corner_eyebrow['dist']=calculate_len(coords[self.right_eye_corner_eyebrow['p1']],coords[self.right_eye_corner_eyebrow['p2']])
        self.left_eye_nose['dist']=calculate_len(coords[self.left_eye_nose['p1']],coords[self.left_eye_nose['p2']])
        self.right_eye_nose['dist']=calculate_len(coords[self.right_eye_nose['p1']],coords[self.right_eye_nose['p2']])
        self.left_eyebrow_nose['dist']=calculate_len(coords[self.left_eyebrow_nose['p1']],coords[self.left_eyebrow_nose['p2']])
        self.right_eyebrow_nose['dist']=calculate_len(coords[self.right_eyebrow_nose['p1']],coords[self.right_eyebrow_nose['p2']])
        self.right_eye_length['dist']=calculate_len(coords[self.right_eye_length['p1']],coords[self.right_eye_length['p2']])
        self.left_eye_length['dist']=calculate_len(coords[self.left_eye_length['p1']],coords[self.left_eye_length['p2']])
    def update_ratio(self):
        self.left_mouth_jaw_ratio=self.jaw_right_left['dist']/self.left_mouth_corner_jaw['dist']
        self.right_mouth_jaw_ratio=self.jaw_right_left['dist']/self.right_mouth_corner_jaw['dist']
        self.right_eyebrow_nose_ratio=self.right_eye_nose['dist']/self.right_eyebrow_nose['dist']
        self.left_eyebrow_nose_ratio=self.left_eye_nose['dist']/self.left_eyebrow_nose['dist']
        self.left_eye_open_ratio=self.left_eye_length['dist']/self.eye_left_up_down['dist']
        self.right_eye_open_ratio=self.right_eye_length['dist']/self.eye_right_up_down['dist']
        

def printing(frame,coords):
    lenghts=Lenghts()
    lenghts.update_len(coords)
    lenghts.update_ratio()
    return [lenghts.left_mouth_jaw_ratio,lenghts.right_mouth_jaw_ratio,lenghts.right_eyebrow_nose_ratio,lenghts.left_eyebrow_nose_ratio,lenghts.left_eye_open_ratio,lenghts.right_eye_open_ratio]