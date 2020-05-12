//
//  unitsViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//


import UIKit
import WebKit
class CommunityViewController: UIViewController,WKNavigationDelegate {
    
    
    @IBOutlet var webView: WKWebView!
    @IBOutlet var communitybackbutton: UIImageView!
    
    @IBOutlet var loading: UILabel!
    @IBOutlet var activityind: UIActivityIndicatorView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let myURL = URL(string:"https://nh.ng.mil/Public-Affairs/Community-Outreach/")
        let myRequest = URLRequest(url: myURL!)
        webView.load(myRequest)
        webView.addSubview(self.activityind)
        self.webView.navigationDelegate = self
        activityind.startAnimating()
        activityind.hidesWhenStopped = true

        
        let tapGesture4 = UITapGestureRecognizer(target: self, action: #selector(imageTapped4))

                    // add it to the image view;
                    communitybackbutton.addGestureRecognizer(tapGesture4)
                    // make sure imageView can be interacted with by user
                communitybackbutton.isUserInteractionEnabled = true
               
                }
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        loading.isHidden = true

               activityind.stopAnimating()
           }
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
               activityind.stopAnimating()
           }
            
        @objc func imageTapped4(gesture: UIGestureRecognizer) {
            loading.isHidden = true

            // if the tapped view is a UIImageView then set it to imageview
        if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
                //Here you can initiate your new ViewController

                }
            }


            // Do any additional setup after loading the view.
        }




