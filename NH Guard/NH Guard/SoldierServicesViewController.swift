//
//  leadershipViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit
class SoldierServicesViewController: UIViewController {
    
    @IBOutlet weak var soldierviewcorner: UIView!
    @IBAction func substancebutton(_ sender: Any) {
        self.performSegue(withIdentifier: "substanceViewSague", sender: self)
    }
    @IBAction func yellowbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "yellowViewSague", sender: self)
    }
    @IBAction func sexbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "sexViewSague", sender: self)
    }
    @IBAction func backbutton(_ sender: Any) {
    self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
    //Here you can initiate your new ViewController
    }
    override func viewDidLoad() {
        self.soldierviewcorner.layer.cornerRadius = 8
        super.viewDidLoad()
    
        }

        // Do any additional setup after loading the view.

            // Do any additional setup after loading the view.
        }




