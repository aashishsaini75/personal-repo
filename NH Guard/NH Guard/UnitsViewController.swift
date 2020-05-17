//
//  unitsViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//


import UIKit
class UnitsViewController: UIViewController {
    
    @IBOutlet weak var unitviewcorner: UIView!
    @IBAction func fieldviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "fieldViewSague", sender: self)
    }
    
    @IBAction func troopviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "troopViewSague", sender: self)
    }
    
    @IBAction func jointviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "jointViewSague", sender: self)
    }
    
    @IBAction func recruitingviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "recruitingViewSague", sender: self)
    }
    
    @IBAction func nharngviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "nharngViewSague", sender: self)
    }
    
    @IBAction func backbutton(_ sender: Any) {
        
    self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
               //Here you can initiate your new ViewController
    }
    
    override func viewDidLoad() {
        self.unitviewcorner.layer.cornerRadius = 8

          super.viewDidLoad()
          }
     
          // Do any additional setup after loading the view.
    
              // Do any additional setup after loading the view.
        }




