//
//  ViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/2/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {

    @IBOutlet var MoreIconPressed: UIImageView!
    @IBOutlet var FBUIview_corner: UIView!
    @IBOutlet var twUIview_corner: UIView!
    @IBOutlet var btUIview_corner: UIButton!
    @IBOutlet var SoldierIconPressed: UIImageView!
    @IBOutlet var ContactButtonPressed: UIImageView!
    @IBOutlet var LeadershipIconPressed: UIImageView!
    @IBOutlet var ContactIconPressed: UIImageView!
    @IBOutlet var UnitIconPressed: UIImageView!
    @IBOutlet var FamilyIconPressed: UIImageView!
    @IBOutlet var NewsIconPressed: UIImageView!
    @IBOutlet var VeterenIconPressed: UIImageView!
    @IBAction func joinbuttonpressed(_ sender: Any) {
        
        self.performSegue(withIdentifier: "joinViewSague", sender: self)
    }
    @IBAction func twitterbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "twitterViewSague", sender: self)
        
    }
    @IBAction func facebookbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "facebookViewSague", sender: self)
    }
    
    @IBAction func leadshipbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "leadershipViewSague", sender: self)
        
    }
    @IBAction func soldierbutton(_ sender: Any) {
             self.performSegue(withIdentifier: "soldierViewSague", sender: self)
    }
    @IBAction func newsbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "newsViewSague", sender: self)
        
    }
    @IBAction func contactbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "contactViewSague", sender: self)
    }
    
    @IBAction func unitsbutton(_ sender: Any) {
         self.performSegue(withIdentifier: "unitViewSague", sender: self)
    }
    @IBAction func veterenbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "veterenViewSague", sender: self)
    }
    
    @IBAction func family(_ sender: Any) {
         self.performSegue(withIdentifier: "familyViewSague", sender: self)
        
    }
    @IBAction func morebutton(_ sender: Any) {
        self.performSegue(withIdentifier: "MoreScreenSague", sender: self)
        
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if #available(iOS 10.3, *) {
        ReviewService().showReviewView(afterMinimumLaunchCount: 10)
        }
        else{
            // Review View is unvailable for lower versions. Please use your custom view.
        }
        
        self.FBUIview_corner.layer.cornerRadius = 25
        self.twUIview_corner.layer.cornerRadius = 25
        self.btUIview_corner.layer.cornerRadius = 8
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(imageTapped))

            // add it to the image view;
            MoreIconPressed.addGestureRecognizer(tapGesture)
            // make sure imageView can be interacted with by user
        MoreIconPressed.isUserInteractionEnabled = true
        
        let tapGesture1 = UITapGestureRecognizer(target: self, action: #selector(imageTapped1))
//
                   // add it to the image view;
            LeadershipIconPressed.addGestureRecognizer(tapGesture1)
                   // make sure imageView can be interacted with by user
        LeadershipIconPressed.isUserInteractionEnabled = true
        let tapGesture2 = UITapGestureRecognizer(target: self, action: #selector(imageTapped2))
        //
                           // add it to the image view;
                    SoldierIconPressed.addGestureRecognizer(tapGesture2)
                           // make sure imageView can be interacted with by user
                SoldierIconPressed.isUserInteractionEnabled = true
        let tapGesture3 = UITapGestureRecognizer(target: self, action: #selector(imageTapped3))
               //
                                  // add it to the image view;
                           NewsIconPressed.addGestureRecognizer(tapGesture3)
                                  // make sure imageView can be interacted with by user
                       NewsIconPressed.isUserInteractionEnabled = true
        let tapGesture4 = UITapGestureRecognizer(target: self, action: #selector(imageTapped4))
        //
                           // add it to the image view;
                    ContactIconPressed.addGestureRecognizer(tapGesture4)
                           // make sure imageView can be interacted with by user
                ContactIconPressed.isUserInteractionEnabled = true
        let tapGesture5 = UITapGestureRecognizer(target: self, action: #selector(imageTapped5))
            //
                               // add it to the image view;
                        UnitIconPressed.addGestureRecognizer(tapGesture5)
                               // make sure imageView can be interacted with by user
                    UnitIconPressed.isUserInteractionEnabled = true
        let tapGesture6 = UITapGestureRecognizer(target: self, action: #selector(imageTapped6))
            //
                               // add it to the image view;
                        FamilyIconPressed.addGestureRecognizer(tapGesture6)
                               // make sure imageView can be interacted with by user
                    FamilyIconPressed.isUserInteractionEnabled = true
        let tapGesture7 = UITapGestureRecognizer(target: self, action: #selector(imageTapped7))
                //
                                   // add it to the image view;
                        VeterenIconPressed.addGestureRecognizer(tapGesture7)
                                   // make sure imageView can be interacted with by user
                    VeterenIconPressed.isUserInteractionEnabled = true
        }
    
    
    @objc func imageTapped(gesture: UIGestureRecognizer) {
            // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "MoreScreenSague", sender: self)
                //Here you can initiate your new ViewController

                }
            }
    @objc func imageTapped1(gesture: UIGestureRecognizer) {
    // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "leadershipViewSague", sender: self)
        //Here you can initiate your new ViewController

                }
            }
    @objc func imageTapped2(gesture: UIGestureRecognizer) {
    // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "soldierViewSague", sender: self)
        //Here you can initiate your new ViewController

                }
            }
    @objc func imageTapped3(gesture: UIGestureRecognizer) {
    // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "newsViewSague", sender: self)
        //Here you can initiate your new ViewController

                }
            }
    @objc func imageTapped4(gesture: UIGestureRecognizer) {
    // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "contactViewSague", sender: self)
        //Here you can initiate your new ViewController

                }
            }
    @objc func imageTapped5(gesture: UIGestureRecognizer) {
      // if the tapped view is a UIImageView then set it to imageview
              if (gesture.view as? UIImageView) != nil {
                  self.performSegue(withIdentifier: "unitViewSague", sender: self)
          //Here you can initiate your new ViewController

                  }
              }
    @objc func imageTapped6(gesture: UIGestureRecognizer) {
       // if the tapped view is a UIImageView then set it to imageview
               if (gesture.view as? UIImageView) != nil {
                   self.performSegue(withIdentifier: "familyViewSague", sender: self)
           //Here you can initiate your new ViewController

                   }
               }
    
        
    @objc func imageTapped7(gesture: UIGestureRecognizer) {
    // if the tapped view is a UIImageView then set it to imageview
            if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "veterenViewSague", sender: self)
        //Here you can initiate your new ViewController

                }
            }
    
  
    
   
        // Do any additional setup after loading the view.
    }



