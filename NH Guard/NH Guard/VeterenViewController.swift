//
//  MoreScreenViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/3/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit

class VeterenViewController: UIViewController {

    @IBOutlet var vtuicont: UIView!
    
    @IBAction func cemetrybutton(_ sender: Any) {
        self.performSegue(withIdentifier: "cemetryViewSague", sender: self)
    }
    
    @IBAction func departmentbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "departmentViewSague", sender: self)
    }
    
    @IBOutlet var backbuttonpressed: UIImageView!
    override func viewDidLoad() {
        self.vtuicont.layer.cornerRadius = 8

        super.viewDidLoad()
        let tapGesture2 = UITapGestureRecognizer(target: self, action: #selector(imageTapped3))

                // add it to the image view;
                backbuttonpressed.addGestureRecognizer(tapGesture2)
                // make sure imageView can be interacted with by user
            backbuttonpressed.isUserInteractionEnabled = true
           
            }
        
        @objc func imageTapped3(gesture: UIGestureRecognizer) {
        // if the tapped view is a UIImageView then set it to imageview
        if (gesture.view as? UIImageView) != nil {
            self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
            //Here you can initiate your new ViewController

            }
        }


        // Do any additional setup after loading the view.
    }


