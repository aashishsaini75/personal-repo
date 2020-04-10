//
//  MoreScreenViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/3/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit

class MoreScreenViewController: UIViewController {
    @IBOutlet var morecont: UIView!
    
    @IBAction func missionbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "missionViewSague", sender: self)
        
    }
    
    @IBAction func historybutton(_ sender: Any) {
        self.performSegue(withIdentifier: "historyViewSague", sender: self)
    }
    @IBAction func communitybutton(_ sender: Any) {
        self.performSegue(withIdentifier: "communityViewSague", sender: self)
    }
    @IBOutlet weak var backbuttonpressed: UIImageView!
    
    @IBOutlet var MissionIconPressed: UIImageView!
    
    @IBOutlet var MissionIconPreseed1: UIImageView!
    override func viewDidLoad() {
        self.morecont.layer.cornerRadius = 8

        super.viewDidLoad()
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(imageTapped))

                // add it to the image view;
                backbuttonpressed.addGestureRecognizer(tapGesture)
                // make sure imageView can be interacted with by user
            backbuttonpressed.isUserInteractionEnabled = true
           
            
    let tapGesture1 = UITapGestureRecognizer(target: self, action: #selector(imageTapped1))

                 // add it to the image view;
                 MissionIconPressed.addGestureRecognizer(tapGesture1)
                 // make sure imageView can be interacted with by user
             MissionIconPressed.isUserInteractionEnabled = true
        let tapGesture2 = UITapGestureRecognizer(target: self, action: #selector(imageTapped2))

            // add it to the image view;
            MissionIconPreseed1.addGestureRecognizer(tapGesture2)
            // make sure imageView can be interacted with by user
        MissionIconPreseed1.isUserInteractionEnabled = true
            
             }
        
        
        @objc func imageTapped(gesture: UIGestureRecognizer) {
        // if the tapped view is a UIImageView then set it to imageview
        if (gesture.view as? UIImageView) != nil {
            self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
            //Here you can initiate your new ViewController

            }
        }
        @objc func imageTapped1(gesture: UIGestureRecognizer) {
            // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "missionViewSague", sender: self)
                //Here you can initiate your new ViewController

                }
            }
        @objc func imageTapped2(gesture: UIGestureRecognizer) {
              // if the tapped view is a UIImageView then set it to imageview
              if (gesture.view as? UIImageView) != nil {
                  self.performSegue(withIdentifier: "missionViewSague", sender: self)
                  //Here you can initiate your new ViewController

                  }
              }


        // Do any additional setup after loading the view.
    

}
