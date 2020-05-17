//
//  unitsViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//


import UIKit
class FamilyViewController: UIViewController {
    
 
    @IBOutlet weak var familyviewcorner: UIView!
    @IBAction func additionalviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "additionalViewSague", sender: self)
    }
    
    @IBAction func stateresviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "stateresViewSague", sender: self)
    }
    
    @IBAction func chaplainviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "chaplainViewSague", sender: self)
    }
    
    @IBAction func stateviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "stateViewSague", sender: self)
    }
    @IBAction func careviewbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "careViewSague", sender: self)
    }
    @IBAction func backbutton(_ sender: Any) {
        self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
    }
    override func viewDidLoad() {
        self.familyviewcorner.layer.cornerRadius = 8

        super.viewDidLoad()
        
            }
    
        }
