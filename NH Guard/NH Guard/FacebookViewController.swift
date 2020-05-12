//
//  unitsViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit
import WebKit
class FacebookViewController: UIViewController, WKNavigationDelegate{
    
    
    @IBOutlet var facebookbackbutton: UIImageView!
    
    @IBOutlet var myWebView: WKWebView!
    @IBOutlet var activityind: UIActivityIndicatorView!
    
   
    @IBOutlet var loading: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        let myURL = URL(string:"https://www.facebook.com/NHMinutemen/")
        let myRequest = URLRequest(url: myURL!)
        myWebView.load(myRequest)
        myWebView.addSubview(self.activityind)
        self.myWebView.navigationDelegate = self
        activityind.startAnimating()
        activityind.hidesWhenStopped = true
        
        let tapGesture4 = UITapGestureRecognizer(target: self, action: #selector(imageTapped4))

                    // add it to the image view;
                    facebookbackbutton.addGestureRecognizer(tapGesture4)
                    // make sure imageView can be interacted with by user
                facebookbackbutton.isUserInteractionEnabled = true
               
                }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        loading.isHidden = true
                  activityind.stopAnimating()
              }
       func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
                  activityind.stopAnimating()
        loading.isHidden = true

              }
            
        @objc func imageTapped4(gesture: UIGestureRecognizer) {
            // if the tapped view is a UIImageView then set it to imageview
        if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
                //Here you can initiate your new ViewController

                }
            }


            // Do any additional setup after loading the view.
        }




