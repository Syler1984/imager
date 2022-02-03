using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using imager.ViewModels;

namespace imager
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void BrowserBtn_(object sender, RoutedEventArgs e)
        {

        }

        private void BrowserBtn_Clicked(object sender, RoutedEventArgs e)
        {
            DataContext = new BrowserViewModel();
        }

        private void SettingsBtn_Clicked(object sender, RoutedEventArgs e)
        {
            DataContext = new SettingsViewModel();
        }
    }
}
